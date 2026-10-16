#!/usr/bin/env bash
grep -q $'\r' "$0" && { echo "deploy.sh has Windows line endings. Run: sed -i 's/\r$//' deploy.sh, then run it again."; exit 1; } #
# Hosts the Ask AI demo on Amazon ECS Express Mode and prints the link for the team.
# Run it in CloudShell, from the folder with app.py and the Dockerfile:
#   APP_PASSWORD='<team password>' bash deploy.sh
# Running it again ships the current app.py to the same link.
# Optional: ASKAI_REGION (default us-east-1), ASKAI_FUNCTION (default askai-poc),
# SUBNETS='subnet-a,subnet-b' (public subnets in two or more AZs) for an account without a default VPC.
set -euo pipefail

# The Lambda's region. CloudShell sets AWS_REGION to whatever region it was opened in, so don't use that.
REGION=${ASKAI_REGION:-us-east-1}
FUNCTION=${ASKAI_FUNCTION:-askai-poc}
NAME=askai-demo
: "${APP_PASSWORD:?Set the password the team will type: APP_PASSWORD='...' bash deploy.sh}"

# Check what would make step 3 fail before building or creating anything.
aws lambda get-function --region "$REGION" --function-name "$FUNCTION" >/dev/null 2>&1 || {
  echo "No Lambda $FUNCTION in $REGION. Set ASKAI_REGION to the function's region." >&2
  exit 1
}
NETWORK=()
if [ -n "${SUBNETS:-}" ]; then
  NETWORK=(--network-configuration "{\"subnets\":[\"${SUBNETS//,/\",\"}\"]}")
elif [ "$(aws ec2 describe-subnets --region "$REGION" --filters Name=default-for-az,Values=true \
          --query 'length(Subnets)' --output text)" = 0 ]; then
  echo "This account has no default VPC in $REGION, which ECS Express Mode uses by default." >&2
  echo "Ask your AWS admin for two public subnet IDs in $REGION, then run: SUBNETS='subnet-aaa,subnet-bbb' APP_PASSWORD='...' bash deploy.sh" >&2
  exit 1
fi

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
REGISTRY=$ACCOUNT.dkr.ecr.$REGION.amazonaws.com
IMAGE=$REGISTRY/$NAME:$(date +%Y%m%d-%H%M%S)

echo "== 1/4 Build the image and push it to ECR"
aws ecr describe-repositories --region "$REGION" --repository-names $NAME >/dev/null 2>&1 \
  || aws ecr create-repository --region "$REGION" --repository-name $NAME >/dev/null
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin "$REGISTRY"
docker build --platform linux/amd64 -t "$IMAGE" .
docker push "$IMAGE"

echo "== 2/4 Create the roles, log group and cluster"
make_role() {  # role name, the AWS service that runs as it
  aws iam get-role --role-name "$1" >/dev/null 2>&1 || aws iam create-role --role-name "$1" \
    --assume-role-policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"$2\"},\"Action\":\"sts:AssumeRole\"}]}" >/dev/null
}
make_role $NAME-execution ecs-tasks.amazonaws.com
aws iam attach-role-policy --role-name $NAME-execution \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
make_role $NAME-infrastructure ecs.amazonaws.com
aws iam attach-role-policy --role-name $NAME-infrastructure \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRoleforExpressGatewayServices
# The app itself may only invoke the Ask AI Lambda.
make_role $NAME-task ecs-tasks.amazonaws.com
aws iam put-role-policy --role-name $NAME-task --policy-name invoke-askai --policy-document \
  "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:$REGION:$ACCOUNT:function:$FUNCTION\"}]}"
aws logs create-log-group --region "$REGION" --log-group-name /ecs/$NAME 2>/dev/null || true
aws ecs create-cluster --region "$REGION" --cluster-name $NAME >/dev/null
# An account's first load balancer needs these service-linked roles. If ECS creates them mid-deploy,
# it can use them before they propagate and the deploy fails, so create them here ("already exists" is fine).
for service in elasticloadbalancing.amazonaws.com ecs.application-autoscaling.amazonaws.com; do
  aws iam create-service-linked-role --aws-service-name $service >/dev/null 2>&1 || true
done

echo "== 3/4 Create or update the service"
CONTAINER=$(IMAGE=$IMAGE REGION=$REGION FUNCTION=$FUNCTION NAME=$NAME python3 -c '
import json, os
env = {"AWS_REGION": os.environ["REGION"], "ASKAI_FUNCTION": os.environ["FUNCTION"], "APP_PASSWORD": os.environ["APP_PASSWORD"]}
print(json.dumps({
    "image": os.environ["IMAGE"],
    "containerPort": 8501,
    "awsLogsConfiguration": {"logGroup": "/ecs/" + os.environ["NAME"], "logStreamPrefix": os.environ["NAME"]},
    "environment": [{"name": k, "value": v} for k, v in env.items()],
}))')
ARN=$(aws ecs list-services --region "$REGION" --cluster $NAME --query 'serviceArns[0]' --output text)
if [ "$ARN" = "None" ] || [ -z "$ARN" ]; then
  sleep 30  # new IAM roles take a little while before AWS services can use them
  # One task only: Streamlit keeps each visitor's session on the task that served the page.
  ARN=$(aws ecs create-express-gateway-service --region "$REGION" --cluster $NAME --service-name $NAME \
    --execution-role-arn arn:aws:iam::$ACCOUNT:role/$NAME-execution \
    --infrastructure-role-arn arn:aws:iam::$ACCOUNT:role/$NAME-infrastructure \
    --task-role-arn arn:aws:iam::$ACCOUNT:role/$NAME-task \
    --primary-container "$CONTAINER" --health-check-path /_stcore/health \
    --cpu 512 --memory 1024 --scaling-target '{"minTaskCount":1,"maxTaskCount":1}' \
    ${NETWORK[@]+"${NETWORK[@]}"} \
    --query service.serviceArn --output text)
else
  aws ecs update-express-gateway-service --region "$REGION" --service-arn "$ARN" \
    --primary-container "$CONTAINER" >/dev/null
fi

echo "== 4/4 Wait for this version to go live (10-15 minutes the first time)"
# ECS moves traffic over in stages. Until only this run's image is active, part of the traffic
# still goes to the previous version, so wait for that before testing the link.
URL=""
for _ in $(seq 1 80); do  # about 15 minutes
  STATE=$(aws ecs describe-express-gateway-service --region "$REGION" --service-arn "$ARN" \
    --query '[length(service.activeConfigurations), service.activeConfigurations[0].primaryContainer.image, service.activeConfigurations[0].ingressPaths[0].endpoint]' \
    --output text 2>/dev/null || true)
  read -r COUNT LIVE HOST <<<"$STATE" || true
  if [ -z "$URL" ] && [ -n "${HOST:-}" ] && [ "$HOST" != "None" ]; then
    URL="https://${HOST#https://}"
    echo "Link (answers once this version is live): $URL"
  fi
  if [ "${COUNT:-}" = 1 ] && [ "${LIVE:-}" = "$IMAGE" ] && [ -n "$URL" ] \
     && curl -fsS -m 10 "$URL/_stcore/health" >/dev/null 2>&1; then
    echo; echo "Ready: $URL"
    echo "The team signs in with the APP_PASSWORD you set."
    exit 0
  fi
  printf .
  sleep 10
done
echo; echo "This version isn't live yet. Link: ${URL:-not assigned yet}"
echo "Check ECS -> Clusters -> $NAME -> Services -> $NAME -> Deployments and Logs, or CloudWatch log group /ecs/$NAME."
echo "If the deployment rolled back with a permissions error on a first run, run this script again."
exit 1
