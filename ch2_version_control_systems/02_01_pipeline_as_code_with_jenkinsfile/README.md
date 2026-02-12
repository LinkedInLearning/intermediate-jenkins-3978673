# 02_01 Pipeline as Code With Jenkinsfile

Anything you configure in the Jenkins UI can typically be captured in the Jenkinsfile.

- A **Jenkinsfile** is a text file that defines a pipeline
- It uses declarative or scripted pipeline syntax
- Because it is text-based, it can be:
  - Stored in a repository
  - Version controlled
  - Reviewed and updated like application code

- A Jenkinsfile can define:
  - Stages and steps
  - Tools (like Maven, JDK, Node)
  - Project options
  - Triggers
  - Environment variables
  - Post-build actions

## Lab: Configure a Pipeline to Use a Jenkinsfile from SCM

In this lab, you will update your existing **First-Pipeline** job to load its pipeline definition from a Git repository instead of defining it directly in the Jenkins UI.

## Overview

In this lab, you will:

- Copy the repository URL for the course exercise files
- Update the pipeline definition to use “Pipeline script from SCM”
- Configure the Git repository settings
- Build the project
- Review the Pipeline Overview

## Prerequisites

Before starting:

- [Your **First-Pipeline** job already exists](../../ch1_pipelines/01_01_create_a_pipeline_project/README.md)
- You have access to the course exercise files repository (public)

## Instructions

### Step 1: Copy the Repository URL

1. Open the course exercise files repository in your browser.
2. Select **Code**.
3. Make sure **HTTPS** is selected.
4. Select the copy icon (stacked squares) to copy the repository URL.

Keep this URL available for the next steps.

### Step 2: Open the Job Configuration

1. In Jenkins, go to your **First-Pipeline** job.
2. Select **Configure**.
3. Scroll down to the **Pipeline** section.

### Step 3: Change the Pipeline Definition

1. In the **Definition** dropdown, change the option to `Pipeline script from SCM`.
2. Under **SCM**, select `Git`.

### Step 4: Configure the Repository

1. In the **Repository URL** field, paste the URL you copied.
2. Leave credentials empty (the repository is public).
3. Under **Branches to build**, change `master` to `main`.

> [!IMPORTANT]
> Many modern repositories use `main` as the default branch, but Jenkins may default to `master`.

### Step 5: Configure the Script Path

1. Locate the **Script Path** field.
2. Ensure it is set to `Jenkinsfile`.

This tells Jenkins to look for a file named `Jenkinsfile` in the root of the repository.

> [!IMPORTANT]
> If a Jenkinsfile were stored in a sub-directory, you would enter that relative path here.

### Step 6: Save and Build

1. Select **Save**.
2. Select **Build Now**.
3. Wait for the pipeline to complete.

### Step 7: Review the Pipeline Overview

1. Select the most recent build from the build history.
2. Select **Pipeline Overview**.

You should now see:

- A **Checkout SCM** stage
- Additional stages defined in the Jenkinsfile

The first stage checks out the repository and loads the pipeline definition. The remaining stages are defined by the Jenkinsfile stored in the repository.

## Challenge Completion

You have successfully completed this lab if:

- The **First-Pipeline** job uses “Pipeline script from SCM”
- The repository URL is configured correctly
- The branch is set to `main`
- The Script Path is set to `Jenkinsfile`
- The build completes successfully
- The Pipeline Overview shows multiple stages, including **Checkout SCM**

You’ve now moved from manually defined pipelines to a pipeline defined as code using a Jenkinsfile.

<!-- FooterStart -->
---
[← 01_08 Solution: Develop a Parameterized Pipeline](../../ch1_pipelines/01_08_solution_develop_a_parameterized_pipeline/README.md) | [02_02 Connect Jenkins to Github →](../02_02_connect_jenkins_to_github/README.md)
<!-- FooterEnd -->
