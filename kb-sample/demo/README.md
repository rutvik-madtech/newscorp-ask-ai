# Ask AI demo app

A small Streamlit page for showing Ask AI to the team. It sends each question to the `askai-poc` Lambda exactly as the portal backend will (question, role, business unit) and shows Claude's answer, the pages it cited and what it searched.

**It answers from the sample docs in `kb-sample/docs`, not real CDL documentation.**

## Run it

You need Python 3.10 or later and AWS credentials that may invoke the function.

```bash
cd kb-sample/demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
AWS_PROFILE=<your-profile> streamlit run app.py
```

The page opens at http://localhost:8501. Run it from this folder so Streamlit picks up `.streamlit/config.toml`, which hides its developer toolbar.

| Variable | Default | What it sets |
|---|---|---|
| `AWS_PROFILE` | your default profile | Which AWS credentials to use |
| `AWS_REGION` | `us-east-1` | The function's region |
| `ASKAI_FUNCTION` | `askai-poc` | The function's name |
| `APP_PASSWORD` | none | A password the page asks for first. Leave it unset on your laptop |

The credentials only need this permission:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "lambda:InvokeFunction",
    "Resource": "arn:aws:lambda:us-east-1:<account-id>:function:askai-poc"
  }]
}
```

Don't start it with `--server.address 0.0.0.0`: anyone who can reach the page would ask questions with your AWS credentials. To share it, host it as below.

## Host it for the team

`deploy.sh` puts the app on Amazon ECS Express Mode, which gives it an HTTPS link. The page asks for a team password first, and the app runs as its own role that may only invoke `askai-poc`. App Runner isn't an option: it closed to new customers on April 30, 2026, and it doesn't support the WebSockets Streamlit needs.

1. Zip this folder as `askai-demo.zip`, with `.streamlit/` but without `.venv/`. On a Mac or Linux, from `kb-sample/demo`:

   ```bash
   zip -r ../askai-demo.zip . -x '.venv/*' '__pycache__/*'
   ```

2. Open CloudShell as an admin. Select **Actions → Upload file** and upload the zip. Any region works: the script deploys next to the Lambda, in us-east-1.
3. Run this from your home folder:

   ```bash
   unzip -o askai-demo.zip -d askai-demo
   cd "$(dirname "$(find askai-demo -name deploy.sh | head -1)")"
   APP_PASSWORD='<team password>' bash deploy.sh
   ```

   The `cd` line finds the folder holding `deploy.sh`, so it works whether or not your zip tool added a folder inside the zip.

The script first checks that the Lambda exists and that the account has a default VPC. It then builds the image, pushes it to ECR, and creates the roles, the log group, an ECS cluster and the Express service, all named `askai-demo`. It prints the link as soon as AWS assigns it, and `Ready` once this version takes all the traffic: 10–15 minutes the first time. Send the team the link and the password. If a first run rolls back with a permissions error while new roles propagate, run it again.

| Variable | Default | When to set it |
|---|---|---|
| `ASKAI_REGION` | `us-east-1` | The Lambda is in another region |
| `ASKAI_FUNCTION` | `askai-poc` | The Lambda has another name |
| `SUBNETS` | the default VPC | The account has no default VPC. Give two or more public subnet IDs in different AZs, such as `SUBNETS='subnet-aaa,subnet-bbb'` |

To ship a change to `app.py`, upload the new file (CloudShell puts it in your home folder), move it into place and run the script again:

```bash
mv ~/app.py ~/askai-demo/app.py && cd ~/askai-demo
APP_PASSWORD='<team password>' bash deploy.sh
```

If you changed more than `app.py`, upload a new zip and repeat step 3 from your home folder.

It runs one task (0.5 vCPU, 1 GB) behind a load balancer. That's roughly $40–60 a month while it runs, plus Bedrock per question. Delete it when the demo period ends. Paste the whole block: it waits for ECS to remove the load balancer before deleting the roles ECS needs to do that.

```bash
R=us-east-1
ARN=$(aws ecs list-services --region $R --cluster askai-demo --query 'serviceArns[0]' --output text)
aws ecs delete-express-gateway-service --region $R --service-arn "$ARN" --query service.status.statusCode --output text
# Wait while ECS stops the task and removes the load balancer (a few minutes)
while s=$(aws ecs describe-express-gateway-service --region $R --service-arn "$ARN" --query service.status.statusCode --output text 2>/dev/null) && [ "$s" != INACTIVE ]; do echo "$s..."; sleep 15; done
aws ecs delete-cluster --region $R --cluster askai-demo --query cluster.status --output text
aws ecr delete-repository --region $R --repository-name askai-demo --force --query repository.repositoryName --output text
aws logs delete-log-group --region $R --log-group-name /ecs/askai-demo
aws iam detach-role-policy --role-name askai-demo-execution --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
aws iam detach-role-policy --role-name askai-demo-infrastructure --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRoleforExpressGatewayServices
aws iam delete-role-policy --role-name askai-demo-task --policy-name invoke-askai
for r in execution task infrastructure; do aws iam delete-role --role-name askai-demo-$r; done
```

## The two views

- **Ask:** a chat. Pick a role and business unit in the sidebar, then type a question or select a sample. Each question is answered on its own; Ask AI doesn't remember earlier ones.
- **Compare:** one question asked for every role, or in every business unit, side by side. **What Ask AI searched** is open in each column, so you can see which pages each user's search returned.

Each answer takes 5–15 seconds and costs a few cents in Bedrock.

## A five-minute demo

1. **A how-to.** Ask view, Power User, Dow Jones: "How do I approve a request from Realtor.com?" Ask AI gives the steps from the Rules of Use page and cites it.
2. **The same question as Agency.** Switch the role to Agency and ask again. Ask AI says Agency users can't approve requests, citing What each role can see. Open **What Ask AI searched**: the Rules of Use page isn't there, because the search never returns it for Agency.
3. **Side by side.** Compare view, demo "Approving requests, by role", **Run**. Power User and Admin find the Rules of Use page; Agency doesn't.
4. **Business units.** Demo "Realtor.com signals, by business unit". The Realtor.com column lists the three signals; the Dow Jones column says the docs it can see don't list them.
5. **What it won't do.** Ask view: "How many people are in my C-suite audience?" (it can't see live data and points to the Audiences page), then "Write me a poem about data" (declined without a search).
