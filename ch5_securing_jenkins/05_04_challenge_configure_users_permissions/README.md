# 05_04 Challenge: Configure Users and Permissions

In this challenge, you’ll configure Jenkins to use **project-based authorization** to safely separate access between multiple teams.

You’ll create user accounts that represent different teams, configure global permissions so users can log in, and then restrict access to jobs by assigning permissions at the **folder level**. When you’re finished, each team will only be able to see and interact with the jobs they’ve been explicitly given access to.

This challenge reinforces how project-based security enables multiple teams to safely share a single Jenkins instance without exposing each other’s pipelines.

## Challenge Tasks

To complete this challenge, you will:

* Enable **Project-based Matrix Authorization Strategy**
* Ensure your own account has full administrative access
* Create two user accounts: `engineering`, `marketing`
* Grant limited global permissions so users can log in
* Create separate folders for Engineering and Marketing
* Configure folder-level permissions so each user can only access their own folder
* Verify permissions by logging in as a non-admin user

This challenge should take 15–20 minutes to complete.

## Prerequisites

Before starting this challenge, make sure you have:

* A running Jenkins server
* An admin account you can log in with

<!-- FooterStart -->
---
[← 05_03 Use Secrets and Credentials](../05_03_use_secrets_credentials/README.md) | [05_05 Solution: Configure Users and Permissions →](../05_05_solution_configure_users_permissions/README.md)
<!-- FooterEnd -->
