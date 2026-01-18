# 05_05 Solution: Configure Users and Permissions

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

## Instructions

### Step 1: Create User Accounts

1. Log in to Jenkins using your **admin account**.
2. From the Jenkins dashboard, select **Manage Jenkins**.
3. Select **Users**.
4. Create the following users: `engineering`, `marketing`
5. Set passwords for each account and confirm the users are created successfully.

You’ll use these accounts to represent two separate teams.

### Step 2: Enable Project-Based Authorization

1. From the Jenkins dashboard, select **Manage Jenkins**.
2. Select **Security**.
3. Under **Authorization**, select **Project-based Matrix Authorization Strategy**.

> [!IMPORTANT]
> When switching authorization strategies, the permission matrix starts empty. Be sure to add permissions before saving.

### Step 3: Configure Global Permissions

1. In the **Project-based Matrix Authorization** section:
   * Add **your admin username**.
   * Grant **all permissions** to your account.
2. Add the following users:`engineering`, `marketing`
3. For both `engineering` and `marketing`: Under **Overall**, select **Read** only.
4. Select **Save**.

This allows users to log in while preventing access to jobs unless permissions are granted at the project level.

### Step 4: Create Team Folders

1. From the Jenkins dashboard, select **New Item**.
2. Create a folder named **Engineering**.
3. Create a second folder named **Marketing**.

These folders will contain the jobs owned by each team.

### Step 5.1: Configure Folder-Level Permissions \- Engineering Folder

1. Open the **Engineering** folder.
2. Select **Configure**.
3. Enable **Project-based security**.
4. Add the `engineering` user.
5. Grant the `engineering` user **all folder and job permissions**.
6. Save the configuration.

### Step 5.2: Configure Folder-Level Permissions \- Marketing Folder

1. Open the **Marketing** folder.
2. Select **Configure**.
3. Enable **Project-based security**.
4. Add the `marketing` user.
5. Grant the `marketing` user **all folder and job permissions**.
6. Save the configuration.

### Step 6: Verify Permissions as a Non-Admin User

1. Open a new browser window or use an incognito/private session.
2. Log in as the **engineering** user.
3. Select the Jenkins logo to return to the dashboard.

Confirm that:

* The **Engineering** folder is visible
* The **Marketing** folder is not visible

This confirms that project-based permissions are working as expected.

## Challenge Completion

To complete this challenge successfully, confirm that:

* Project-based authorization is enabled
* Your admin account retains full access
* The `engineering` and `marketing` users can log in
* Each user can only see and access their own folder
* No team can view or interact with the other team’s jobs

<!-- FooterStart -->
---
[← 05_04 Challenge: Configure Users and Permissions](../05_04_challenge_configure_users_permissions/README.md) | [06_01 Next Steps →](../../ch6_conclusion/06_01_next_steps/README.md)
<!-- FooterEnd -->
