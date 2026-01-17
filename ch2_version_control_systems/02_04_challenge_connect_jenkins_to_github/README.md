# 02_04 Challenge: Connect Jenkins to Github

In this challenge you’ll connect a GitHub repository and a Jenkins project to implement continuous integration (CI).  The goal is to configure GitHub to send webhooks to Jenkins so the job is triggered when a change is pushed to the repo.

## Challenge Tasks

- Create a new GitHub repo and add the exercise files for this lesson.
- Create a new pipeline project that pulls the code from the repo and uses the Jenkinsfile for the project definition.
- Configure the repository and the pipeline project to allow pushes to the repo to trigger the pipeline.

This challenge should take **15–20 minutes** to complete.

## Prerequisites

To connect Jenkins and GitHub, you need to have the following in place:

- A Jenkins server that is publicly accessible on the internet. Follow the steps in the exercise files document “[Deploy a Jenkins Server](http://../../ch0_introduction/00_02_deploy_a_jenkins_server/README.md)” for details on setting up a Jenkins server.
- A GitHub account

<!-- FooterStart -->
---
[← 02_03 Run Scripts From the Pipeline](../02_03_run_scripts_from_the_pipeline/README.md) | [02_05 Solution: Connect Jenkins to Github →](../02_05_solution_connect_jenkins_to_github/README.md)
<!-- FooterEnd -->
