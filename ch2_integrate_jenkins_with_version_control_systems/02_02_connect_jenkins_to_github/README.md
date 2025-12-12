# 02_02 Connect Jenkins to Github

Jenkins can retrieve pipeline configurations from version control systems like GitHub.  In turn, GitHub can send webhooks to Jenkins so jobs are triggered when a change is pushed to a repo.

To connect Jenkins and GitHub, you need to have the following in place:

- A Jenkins server that is publicly accessible on the internet
- A GitHub account

Follow the steps in [Deploy a Jenkins Server](../../ch0_introduction/00_02_deploy_a_jenkins_server/README.md) for details on setting up a Jenkins server.

## Steps to connect Jenkins to GitHub

1. [Create a new, public repo on GitHub](https://github.new) and include a README.md file during the creation process.

    - Click `Add a file` -> `Create new file`.
    - Name the file `Jenkinsfile`.
    - Copy the contents of the [`Jenkinsfile` for this lesson](./Jenkinsfile) and paste into the file in the new repo.
    - Select `Commit directly to the main branch.`
    - Select `Commit new file`.
    - Select the `Code` button.
    - Select `HTTPS`.
    - Select the stacked squares icon to copy the repo URL to the clipboard.

1. Create a new pipeline project in your Jenkins server.

    - Select `New Item`
    - Enter item name (use the same name as your repo if possible)
    - Select `Pipeline` project
    - `OK`
    - Select `GitHub Project` and paste in the repo URL.
    - *NOTE: This step is optional.  It only creates a link to the repo on the project home page.*
    - Under `Build Triggers`, select the checkbox next to `GitHub hook trigger for GITScm polling`.
    - Under `Pipeline`, select `Pipeline script from SCM`.
    - Under SCM, select `Git`.
    - Under `Repository URL`, paste in the repo URL.
    - Under `Branch Specifier (blank for 'any')`, change `master` to `main`.
    - `Save` &rarr; `Build Now`.
    - *NOTE: The project must run at least one successful build before connecting to GitHub.  This allows Jenkins to read the configuration from the repo.*
    - Copy the URL of your Jenkins server.

1. Go back to the GitHub repo and configure the settings to create a webhook for the project you just created.

    - Select `Settings` &rarr; `Webhooks` &rarr; `Add webhook`.
    - Under `Payload URL`, paste in the URL for your Jenkins server.
    - Immediately after the Jenkins server URL, add `/github-webhook/`.
    - *NOTE: Please be sure to include the trailing slash on `github-webhook/`.  The field should be in a format similar to `http://your-jenkins-server.com/github-webhook/`.*
    - Under `Content type`, select `application/json`.
    - `Add webhook`
    - *NOTE: GitHub will ping the Jenkins server and indicate a successful connection with a green checkmark next to the webhook name.  If your webhook does not indicate that it connected successfully, select `Edit` and confirm your settings again.  If needed, delete the webhook and start over.*
    - Select the `<>Code` tab.
    - Make a change to the README.md file.
        - Click the pencil icon.
        - Make a change to the file.
        - Click `Commit changes`.
    - Go to the Jenkins server and observe the job being triggered by the change you just made in GitHub.

    - *NOTE: If your job is not triggered, review the configuration for the Jenkins job and the GitHub repo, making any adjustments as needed.  If needed, start again with a new job in Jenkins or with a new webhook in GitHub.*

<!-- FooterStart -->
---
[← 02_01 Pipeline as Code With Jenkinsfile](../02_01_pipeline_as_code_with_jenkinsfile/README.md) | [02_03 Run Scripts From the Pipeline →](../02_03_run_scripts_from_the_pipeline/README.md)
<!-- FooterEnd -->
