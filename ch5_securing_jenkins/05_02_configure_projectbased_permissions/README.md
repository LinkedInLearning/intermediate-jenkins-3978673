# 05_02 Configure Project-Based Permissions

Project-based authorization allows you to control who can access or manage specific jobs and folders, rather than applying permissions globally across Jenkins.

**Use project-based authorization when:**

- Global permissions are too broad
- Different teams own different jobs or folders
- Non-admin users should only build or view specific projects

**How project-based authorization works:**

- Permissions are defined at the folder or job level
- Users can have different permissions on different projects, folders, and jobs
- Access can be granted by user or group

## Best Practices with Project-based Authorization

- Enable Project-based Matrix Authorization Strategy
- Define minimal global permissions (often read-only)
- Assign detailed permissions inside folders; Prefer folders over individual job permissions
- Group related jobs into folders to simplify management
- Grant the least privilege necessary

## Lab: Configure Project-Based Authorization in Jenkins

In this lab, you’ll configure **project-based authorization** in Jenkins to restrict a user’s access to specific folders and jobs. You’ll compare how permissions behave globally versus at the folder level and see the changes immediately from a non-admin user’s perspective.

### Prerequisites

Before starting this lab, make sure you have:

- A running Jenkins server
- Completed the **previous lab on matrix-based authorization**
- An additional non-admin user account (for example, `nicole`)
- Two browser windows or tabs open:

  - One logged in as an **admin**
  - One logged in as the **non-admin user**

### Instructions

#### 1. Switch to Project-Based Authorization

1. Log in to Jenkins using your **admin account**.
2. From the Jenkins dashboard, select **Manage Jenkins**.
3. Select **Security**.
4. Under **Authorization**, locate **Project-based Matrix Authorization Strategy**.
5. Carefully select **Project-based Matrix Authorization Strategy**.

> [!IMPORTANT]
> When switching from matrix-based authorization to project-based authorization, **existing permissions are not preserved**. Be sure you understand which users and permissions you need before saving changes.

#### 2. Recreate Global Permissions

Since the permission matrix is now empty, you’ll need to add users again.

1. Select **Add user**.
2. Enter your **admin username** (use your own username).
3. Select **OK**.
4. Select **Grant all permissions** for your admin user.
5. Next, add the non-admin user:

    - Select **Add user**.
    - Enter the username of your non-admin user (for example, `nicole`).
    - Select **OK**.

6. Limit the non-admin user to "read only" permissions:

   - Under **Overall**, select **Read**

7. Select **Save**.

#### 3. Verify Access as the Non-Admin User

1. Switch to the browser window logged in as the **non-admin user**.
2. Reload the page.

You should notice that **no jobs or folders are visible**.
This is expected because project-level permissions have not been configured yet.

#### 4. Create and Prepare a Folder for Project-Based Permissions

1. Switch back to the **admin account**.
2. From the Jenkins dashboard, select **New Item**.
3. Enter the name `Reports`.
4. Select **Folder**, then select **OK**.
5. Move at least one existing job into the `Reports` folder:

   - Browse to a job's homepage.
   - Select **Move**.
   - For the destination, select the the `Reports` folder
   - Select **Move**.

#### 5. Enable Project-Based Security on the Folder

1. Open the `Reports` folder.
2. Select **Configure**.
3. Enable **Project-based security** by selecting the checkbox.

#### 6. Assign Folder-Level Permissions

1. Under the folder’s permission matrix, select **Add user**.
2. Enter the non-admin username (for example, `nicole`).
3. Select **OK**.
4. Under **Job**, select:

   - **Build**
   - **Cancel**
   - **Read**
   - **Workspace**

5. Select **Apply**.

#### 7. Confirm Folder Access as the Non-Admin User

1. Switch to the browser window logged in as the **non-admin user**.
2. Reload the page.  You should now see the **Reports** folder.
3. Open the **Reports** folder.
4. Verify that the jobs inside the folder are visible and accessible based on the permissions you assigned.

## Next Steps

In the next lesson you'll explore how to store secrets and credentials in Jenkins and then how to apply them securely in a pipeline configuration.

## Shenanigans

### 1. **“They can delete the folder too!?”**

Two Jenkins admins are discussing how to set project-based authorization.

**Admin 1 (Explaining):**  Alright, so here’s something important to know about project-based authorization. If you give a user **Job → Delete** permissions using the permission matrix...

**Admin 2 (Casual):**  ...They can delete jobs inside the folder. That tracks.

**Admin 1:**  Not just the jobs. They can delete the **entire folder** too.

**Admin 2 (Incredulous):**  They can delete the folder too!?

**Admin 1:**  Yep. Folder gone. And when the folder goes...

**Admin 2:**  ...all the jobs inside it go too?

**Admin 1:**  Exactly. No folder, no jobs.

**Admin 2 (Pause):**  Wait...the whole folder?

**Admin 1:**  Sure. And here’s the kicker: once the folder is gone, if that user doesn’t have permissions anywhere else, Jenkins falls back to whatever permissions they have at the **global project-based level**.

**Admin 2:**  So if we followed best practices...

**Admin 1:**  They’re probably read-only globally.

**Admin 2 (face palm, with understanding):**  So they delete the folder, all the jobs are gone, and they lose access to everything.

**Admin 1:**  Welcome to Jenkins permission shenanigans!

**Admin 2:**  Ok...so...yeah...maybe we don’t give *Delete* permission to everyone.

<!-- FooterStart -->
---
[← 05_01 Secure Jenkins With User accounts](../05_01_secure_jenkins_with_user_accounts/README.md) | [05_03 Use Secrets and Credentials →](../05_03_use_secrets_credentials/README.md)
<!-- FooterEnd -->
