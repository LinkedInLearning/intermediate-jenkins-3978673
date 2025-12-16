# 05_01 Secure Jenkins With User accounts

Jenkins provides security features by default.  For example, new installations are locked and require an initial admin password.

Jenkins also allows you to create user accounts with usernames and passwords to control who can log in.

- **Everyone is an admin by default**: The default authorization allows all authenticated users to perform any operations.

- A best practice is to limit admin permission to a few, select users and give limited permissions to other users as needed.

- **Matrix-based Security**: To configure user permissions, most Jenkins installations will use the [Matrix authorization strategy plugin](https://plugins.jenkins.io/matrix-auth/).  This is one of the suggested plugins that gets installed in most Jenkins installations.

  - **Permissions are assigned to each user individually**.
  - **Each user is given specific permission to perform certain actions**.

> [!CAUTION]
> When setting up Matrix-based security, please be sure to give your user administrative permissions.
> If you do not assign admin permissions to your account, **you run the risk of locking yourself out of your Jenkins server**.

## Resources

View the following documents for more information on security configurations in Jenkins.

| Resource | Description |
|----------|-------------|
| [Managing Security](https://www.jenkins.io/doc/book/security/managing-security/) | An overview of access control, [security realms](#1-security-realms), and authorization |
| [Permissions](https://www.jenkins.io/doc/book/security/permissions/) | An overview of permissions in the Jenkins system |
| [Disable Access Control](https://www.jenkins.io/doc/book/security/access-control/disable/) | ⚠️ **Steps to take if you get locked out!** ⚠️|

## Lab: Configure Matrix-Based Security in Jenkins

In this lab, you’ll configure Jenkins security using **matrix-based authorization**. You’ll create a non-admin user, assign permissions explicitly, and verify how those permissions affect what the user can see and do in the Jenkins interface.

This exercise will help you understand how Jenkins transitions from its default “everyone is an admin” model to a more secure, role-aware configuration.

### Prerequisites

Before starting this lab, make sure you have:

- Administrator access to a Jenkins server
- The Jenkins server should have at least one existing job

## Step 1: Create a user account

1. Log in to Jenkins using an administrator account.
2. Navigate to the **Users** page.
3. From the **Users** page, select **Create User**.
4. Enter the following details:

   - **Username**: Choose a username for a non-admin user (for example, `nicole`)
   - **Password**: Enter a password
   - **Full Name**: Enter a full name
   - **Email Address**: Enter an email address

5. Select **Create User** to save the account.

At this point, the user exists but does not yet have clearly defined permissions.

## Step 2: Enable Matrix-Based Security

1. Browse to the **Manage Jenkins** menu.
2. Select **Security**.
3. In the **Authorization** section, confirm that the current authorization strategy set to allow logged-in users to do anything.
4. Select the **Authorization** drop down menu and select **Matrix-based security**.

## Step 3: Add Your Admin Account to the Matrix

Before saving any changes, you must explicitly grant permissions to your own account.

1. At the bottom of the permission matrix, select **Add user...**.
2. Enter your user ID and select **OK** to add your user to the matrix.
3. On the row with your user ID, select the checkbox under **Overall → Administer** permission.
4. (Optional but recommended) Select the **Grant all permissions** icon for your user to clearly mark it as an administrator.

> [!CAUTION]
> If you don't grant yourself admin permissions before saving changes, you may lock yourself out of Jenkins.

## Step 4: Add Permissions for the Non-Admin User

1. Add the the username you created earlier to the permission matrix.
2. In the row for the additional user, select **Read** under the **Overall** section.
3. Under the **Job** section, select the following permissions:

   - **Build**
   - **Cancel**
   - **Read**
   - **Workspace**

Do **not** grant permissions for:

- Overall → Administer
- Credentials
- Agents
- Job → Configure or Job → Delete

This ensures the user can interact with jobs without changing them and cannot manage Jenkins itself.

## Step 5: Save the Security Configuration

1. Scroll to the bottom of the page.
2. Select **Save**.

> [!IMPORTANT]
> When the security configuration is modified and saved, the changes take effect immediately.

## Step 6: Verify Permissions by Logging in as the Non-Admin User

1. Select the user menu in the top-right corner.
2. Sign out of Jenkins.
3. Sign back in using the non-admin user credentials.
4. Observe the Jenkins interface:

    - The **Manage Jenkins** link is no longer visible.
    - The **New Item** link is missing.

5. Open an existing Jenkins job (for example, `publish-reports`).
6. Confirm that the user **is able to**:

    - Trigger a build
    - View build history
    - Access test reports or workspaces

7. Confirm that the user **cannot**:

    - Configure the job
    - Delete the job
    - Modify global Jenkins settings

This confirms that matrix-based security is working as expected.

## Next Steps

In the next lesson, you'll explore the Project-Based Matrix Authorization Strategy, which allows you to define permissions at the individual job or folder level instead of applying permissions globally.

## Shenanigans

### 1. Security Realms

Jenkins can be configured to use different [security realms](https://www.jenkins.io/doc/book/security/managing-security/#security-realm).

Using a very brief explanation, a security realm controls how a person is authenticated to access a resource.

The default realm is a user database included in the Jenkins server.  This is where Jenkins creates the first users with permission to access the system when the service is installed.

Jenkins can also delegate authorization to other realms including:

- Services that provide [Lightweight Directory Access Protocol (LDAP)](https://plugins.jenkins.io/ldap/)
- Systems that support Unix-style [Pluggable Authentication Module](https://plugins.jenkins.io/pam-auth/) users and groups.

<!-- FooterStart -->
---
[← 04_06 Solution: Create artifacts and Reports](../../ch4_artifacts_and_testing/04_06_solution_create_artifacts_reports/README.md) | [05_02 Configure Project-Based Permissions →](../05_02_configure_projectbased_permissions/README.md)
<!-- FooterEnd -->
