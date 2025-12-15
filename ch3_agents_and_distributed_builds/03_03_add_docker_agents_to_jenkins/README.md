# 03_03 Add Docker Agents to Jenkins

- Docker agents provide isolated, repeatable build environments
- Jenkins dynamically creates and removes Docker-based agents
- The Docker Plugin connects Jenkins directly to the local Docker daemon
- Pipelines fully define the build environment via container images

> [!NOTE]
> Configure Jenkins to run pipeline jobs inside Docker containers using Docker-based agents.

## Prerequisites

- Jenkins server (controller) with:
  - Docker installed and running
  - Sufficient disk space for images
  - Enough memory to run containers
- Jenkins user allowed to access Docker
- Docker Plugin installed in Jenkins

## Step 1: Verify Docker on the Jenkins Server

- Open a terminal on the Jenkins server
- Become the `jenkins` user: `sudo su jenkins -s /bin/bash`
- Confirm Docker is installed: `docker --version`
- Confirm Docker service is running: `bash docker ps`
- Successful output confirms Jenkins can communicate with Docker

## Step 2: Install the Docker Plugin

- In Jenkins:
  - **Manage Jenkins → Clouds → Install a plugin**
- Filter plugins by cloud providers
- Select **Docker Plugin**
- Install and return to **Manage Jenkins**

## Step 3: Configure a Docker Cloud

- Navigate to:
  - **Manage Jenkins → Clouds → New Cloud**
- Cloud name: `docker-cloud`
- Cloud type: **Docker**
- Docker Host URI: `unix:///var/run/docker.sock`
  - (Use the help icon to copy the default value)
- Enable the Docker cloud
- Save the configuration

## Step 4: Run a Pipeline Using a Docker Agent

- Create a pipeline job using the provided [Jenkinsfile for this lesson](./Jenkinsfile).
- Run the job
- Open the job’s **Console Output**
- Confirm the pipeline runs inside the specified Docker image

<!-- FooterStart -->
---
[← 03_02 Add an SSH agent to Jenkins](../03_02_add_an_ssh_agent_to_jenkins/README.md) | [03_04 Challenge: Improve a Docker Agent Pipeline →](../03_04_challenge_improve_a_docker_agent_pipeline/README.md)
<!-- FooterEnd -->
