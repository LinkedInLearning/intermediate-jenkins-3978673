# 03_02 Add an SSH agent to Jenkins

- SSH agents allow Jenkins to offload work from the controller
- Labels are how pipelines select specific agents
- CloudFormation simplifies repeatable agent provisioning
- SSH credentials are managed securely inside Jenkins

> [!NOTE]
> Add a Linux node to Jenkins using SSH so pipeline jobs can run on an external agent.

## Prerequisites

- Jenkins server up and running (controller)
- Linux server reachable from Jenkins over SSH

  - Deployed via provided CloudFormation template **or**
  - Any existing Linux host
- SSH access (user + private key)
- Jenkins user allowed to connect on port 22

## Step 1: Deploy the Linux SSH Agent (AWS)

- Open **CloudFormation**
- Create a new stack using the provided template:

  - Upload [`ssh-agent-cloudformation-template.yml`](./ssh-agent-cloudformation-template.yml)
- Stack details:

  - Stack name: `linux-node`
  - Jenkins stack reference: `jenkins-server`
- Acknowledge IAM resource creation
- Submit and wait for stack creation (~4 minutes)

- Key Outputs to Note
  - Linux node **private DNS name**
  - Link to the **private SSH key** (stored in Parameter Store)
  - Optional: link to open a terminal session for troubleshooting

## Step 2: Create a New Jenkins Node

- In Jenkins:
  - **Manage Jenkins → Nodes → New Node**
    - Node name: `linux-node`
    - Node type: **Permanent Agent**
    - Remote root directory: `/home/ec2-user`

- Labels: `linux-node`
- Launch method: **Launch agents via SSH**

## Step 3: Configure SSH Connection

- Host: Paste the **private DNS name** from CloudFormation
- Credentials:
  - Type: **SSH username with private key**
  - ID / Description: `linux-node`
  - Username: `ec2-user`
  - Private key:
    - Select **Enter directly**
    - Paste key from Parameter Store (Show decrypted value)
- Host Key Verification: **Non-verifying verification strategy**
- Save the node configuration

## Step 4: Verify Agent Connection

- Open the node details
- View the **log**
- Confirm status:
  - Agent is connected
  - Node is **online**

## Step 5: Use the SSH Agent in a Pipeline

- Create a pipeline job using the provided [Jenkinsfile for this lesson](./Jenkinsfile).
- Run the job
- Confirm output shows: `Running on linux-node`
- Verify job completes successfully

<!-- FooterStart -->
---
[← 03_01 Distribute Builds With Agents](../03_01_distribute_builds_with_agents/README.md) | [03_03 Add Docker Agents to Jenkins →](../03_03_add_docker_agents_to_jenkins/README.md)
<!-- FooterEnd -->
