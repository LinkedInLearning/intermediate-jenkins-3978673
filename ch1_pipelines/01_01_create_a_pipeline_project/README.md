# 01_01 Create a Pipeline Project

Pipelines are the most efficient way to define and manage projects in Jenkins. Using a declarative pipeline, you can capture your entire build configuration as code.

In this lab, you’ll create your very first pipeline project and use a sample configuration to print a familiar message: **Hello World**.

## Overview

In this lab, you will:

- Create a new Pipeline project in Jenkins
- Use a built-in sample pipeline script
- Run the pipeline
- View the Pipeline Overview visualization

By the end of this lab, you’ll understand how to create and execute a basic declarative pipeline.

## Prerequisites

Before you begin, make sure you have:

- Access to a running Jenkins server
- Permission to create new jobs
- A user account logged into Jenkins

## Lab Tasks

To complete this lab, you will:

- Create a new Pipeline job
- Configure the job using a sample pipeline script
- Run the pipeline
- Review the pipeline output and visualization

## Instructions

### Step 1: Create a New Pipeline Job

1. From the Jenkins dashboard, select **New Item**.

2. In the **Item name** field, enter: `First-Pipeline`

3. Select the **Pipeline** project type.

4. Select **OK**.

You will now be on the job configuration screen.

### Step 2: Configure the Pipeline Script

1. Scroll down to the **Pipeline** section.
2. In the **Definition** area, locate the **Script** box.
3. Select the drop-down menu next to the script field.
4. Choose **Try a sample Pipeline**.
5. Select **Hello World** from the list.

You should now see a sample declarative pipeline script automatically populated in the script editor.

This sample pipeline defines:

- An agent
- A stage
- A step that prints “Hello World”

### Step 3: Save the Job

1. Select **Save**.

You will be redirected to the project’s main page.

### Step 4: Build the Pipeline

1. On the left-hand side of the project page, select **Build Now**.
2. Wait for the pipeline run to complete.
3. Observe the build status indicator next to the job name.

Once the build finishes successfully, you should see a green status icon.

### Step 5: View the Pipeline Overview

1. Select the drop-down arrow next to the completed build in the build history.
2. Select **Pipeline Overview**.

The Pipeline Overview provides:

- A visual representation of the pipeline stages
- Execution status for each stage
- The output message from the pipeline

You should see the successful stage along with the “Hello World” message in the logs.

## Lab Completion

You have successfully completed this lab if:

- A job named **First-Pipeline** exists in your Jenkins dashboard
- The pipeline builds successfully
- The Pipeline Overview shows a completed stage
- The console output displays the expected message

In the next lesson, you’ll take a closer look at each part of a pipeline configuration and begin customizing your own.

<!-- FooterStart -->
---
[← 00_02 Deploy a Jenkins Server](../../ch0_introduction/00_02_deploy_a_jenkins_server/README.md) | [01_02 Use Build Steps in a Pipeline →](../01_02_use_build_steps_in_a_pipeline/README.md)
<!-- FooterEnd -->
