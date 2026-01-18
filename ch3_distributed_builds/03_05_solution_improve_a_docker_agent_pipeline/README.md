# 03_05 Solution: Improve a Docker Agent Pipeline

In this challenge, you’ll configure Jenkins to run pipeline jobs using a **Docker-based agent**. You’ll confirm Docker is available on the Jenkins server, configure Jenkins to communicate with Docker using the Docker Plugin, and then improve an existing pipeline so it takes full advantage of Docker agents, stages, and steps.

This challenge reinforces how Jenkins dynamically provisions build environments using Docker containers and how pipelines define their execution environment as code.

## Challenge Tasks

To complete this challenge, you will:

* Confirm Docker is installed and accessible on the Jenkins server
* Install and configure the Docker Plugin
* Create a Docker Cloud on the Jenkins controller
* Run a pipeline that uses a Docker agent
* Improve the pipeline by organizing it into clear stages and steps

This challenge should take 10-15 minutes to complete.

## Prerequisites

Before you begin, make sure you have:

* Admin access to a running Jenkins server
* Terminal access to the server where Jenkins is running

## Instructions

### Step 1: Confirm Docker is Installed on the Jenkins Server

1. Open a terminal session connected to the server where Jenkins is running.
2. Switch to the `jenkins` user: `sudo su jenkins -s /bin/bash`
3. Confirm you are running as the correct user: `whoami`
4. Verify Docker is installed: `docker --version`
5. Confirm the Docker service is running: `docker ps`

If Docker is installed and the service is running, Jenkins will be able to issue Docker commands when using Docker-based agents.

### Step 2: Install the Docker Plugin

1. In the Jenkins web interface, navigate to: **Manage Jenkins → Clouds → Install a plugin**
2. Filter the available plugins by cloud providers.
3. Locate and select the **Docker Plugin**.
4. Install the plugin.
5. When the installation completes, return to **Manage Jenkins**.

### Step 3: Create and Configure a Docker Cloud

1. From **Manage Jenkins**, select **Clouds**.
2. Select **New Cloud**.
3. Enter a name for the cloud: `docker-cloud`
4. Select **Docker** as the cloud type.
5. In the **Docker Host URI** field: `unix:///var/run/docker.sock`
6. Enable the Docker cloud by selecting the **Enabled** checkbox.
7. Save the configuration.

> [!IMPORTANT]
> When pasting the Docker Host URI, make sure there are no trailing spaces. Extra spaces can cause the Docker cloud to fail silently until a job attempts to run.

### Step 4: Run the Pipeline Using a Docker Agent

1. Create a pipeline job using the [Jenkinsfile in the exercise files](./Jenkinsfile).
2. Confirm the pipeline is configured to use a Docker agent.
3. Save the job.
4. Select **Build Now**.
5. When the job completes, open the **Console Output**.
6. Look for log messages indicating that Jenkins is:
   * Launching a new Docker node
   * Pulling or using the specified Docker image

This confirms that Jenkins is successfully running the pipeline inside a Docker container.

### Step 5: Improve the Pipeline Configuration

1. Edit the pipeline job. Update the pipeline to:
   * Define clear `stages`
   * Use `steps` within each stage
   * Improve readability and structure

2. Save your changes.
3. Run the pipeline again.
4. Confirm the job completes successfully using the Docker agent and the updated pipeline structure.

## Challenge Completion

You have completed this challenge when:

* Docker is verified as installed and running on the Jenkins server
* The Docker Plugin is installed and configured
* A Docker Cloud exists and is enabled in Jenkins
* A pipeline successfully runs using a Docker-based agent
* The pipeline is organized into clear stages and steps

Compare your implementation to the solution: [Jenkinsfile](./Jenkinsfile).

<!-- FooterStart -->
---
[← 03_04 Challenge: Improve a Docker Agent Pipeline](../03_04_challenge_improve_a_docker_agent_pipeline/README.md) | [04_01 Artifacts and Fingerprinting →](../../ch4_artifacts_and_testing/04_01_artifacts_fingerprinting/README.md)
<!-- FooterEnd -->
