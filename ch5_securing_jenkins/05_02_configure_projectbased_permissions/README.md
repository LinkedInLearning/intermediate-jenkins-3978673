# 05_02 Configure Project-Based Permissions

## Shenanigans

### 1. Delete the folder too!?

If a user has "Delete" permissions at the folder level using the project-based authorization matrix, they can delete jobs inside the folder _and_ the folder as well!

If the user removes the folder, all jobs inside the folder will be removed as well.

Also, if they don't have any other permissions, their account will default to the permissions given in the  configuration for project-based matrix authorization.  If best practices have been followed, their permissions will likely be read only.

<!-- FooterStart -->
---
[← 05_01 Secure Jenkins With User accounts](../05_01_secure_jenkins_with_user_accounts/README.md) | [05_03 Use Secrets and Credentials →](../05_03_use_secrets_credentials/README.md)
<!-- FooterEnd -->
