# AWS access for building Ask AI in the News Corp account

What the News Corp AWS admin needs to set up so we can build Ask AI. It covers the knowledge base, the Ask AI Lambda and their logs. It doesn't cover the team demo app or the portal.

The permissions are what the proof of concept needed in the dev account, plus what the plan's build stories add (Lambda versions and concurrency, the dashboard and alarm). The files were checked with IAM Access Analyzer (no findings) and the IAM policy simulator.

## What to create

| # | What | Type | Policy file | Trust file |
|---|---|---|---|---|
| 1 | The build user, or a role the build user assumes | IAM user or role | `askai-builder-policy.json` | |
| 2 | `askai-lambda-role`, the role the Ask AI Lambda runs as | IAM role | `askai-lambda-role-policy.json` | `askai-lambda-role-trust.json` |
| 3 | `askai-kb-role`, the role the knowledge base uses to read the articles | IAM role | `askai-kb-role-policy.json` | `askai-kb-role-trust.json` |

The admin creates roles 2 and 3. The build user can't create or change IAM roles; it can only pass these two roles to Lambda and Bedrock.

Before using the files, replace the placeholders:

| Placeholder | Value |
|---|---|
| `ACCOUNT_ID` | The News Corp AWS account ID |
| `REGION` | The region agreed for Ask AI (NWS1-192), for example `us-east-1` |
| `KB_ID` | The knowledge base ID. It exists only after the knowledge base is created, so set it in `askai-lambda-role-policy.json` then |

## What the build user can do

Everything is limited to resources whose names start with `askai-`:

| Service | What for | Names it can touch |
|---|---|---|
| S3 | The bucket of help articles | `askai-*` buckets |
| S3 Vectors | The vector store behind the knowledge base | `askai-*` vector buckets |
| Bedrock Knowledge Bases | Create the knowledge base, sync the articles, test searches | Knowledge bases in the account. The IDs are random, so they can't be limited by name |
| Bedrock models | Test calls to Claude Opus 5.5, Titan Text Embeddings V2 and Cohere Rerank 3.5 | Those three models only |
| Lambda | Deploy and test the Ask AI function and its library layer | `askai-*` functions and layers |
| IAM | Pass the two roles above | `askai-lambda-role` and `askai-kb-role` only |
| CloudWatch Logs | Read the Lambda's logs and set how long they're kept | `/aws/lambda/askai-*` |
| CloudWatch | The Ask AI dashboard and alarm (NWS1-244) | `askai-*` dashboards and alarms |

It also gets list and read-only access, for example to see the models and roles in the console.

## Names we'll use

| Resource | Name |
|---|---|
| Help articles bucket | `askai-docs-ACCOUNT_ID` (articles under `docs/`) |
| Vector bucket and index | `askai-vectors-ACCOUNT_ID`, index `askai-docs-index` |
| Knowledge base | `askai-kb` |
| Lambda function | `askai-answer` |
| Lambda layer | `askai-anthropic-sdk` |
| Log group | `/aws/lambda/askai-answer` |

## One-time steps for the admin

1. **Model access.** In the Bedrock console, open Model access and enable Claude Opus 5.5 and Cohere Rerank 3.5 in the Ask AI region. These are AWS Marketplace models, and enabling them needs Marketplace subscribe permission, which the build user doesn't have. Titan Text Embeddings V2 needs no subscription.
2. **Portal backend access (later, NWS1-243).** The portal backend's own role needs `lambda:InvokeFunction` on `arn:aws:lambda:REGION:ACCOUNT_ID:function:askai-answer`. That's part of the portal backend's setup, not this user.

## Not included

- **The team demo app** (ECS, load balancer, container registry). It's only for the proof of concept.
- **Bedrock Guardrails.** They're out of phase 1.
- **CDK or Terraform.** If we deploy with CDK (NWS1-240), the account needs `cdk bootstrap` once, and the build user needs `sts:AssumeRole` on the `cdk-*` roles. Those roles have wider rights, so it's the security team's call; until then we deploy with the AWS CLI using these permissions.
- **Customer-managed KMS keys.** The bucket uses S3's default encryption. If News Corp requires its own KMS key, the two roles and the build user also need `kms:Decrypt` and `kms:GenerateDataKey` on that key.
