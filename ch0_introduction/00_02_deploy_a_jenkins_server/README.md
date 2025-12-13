# 00_02 Deploy a Jenkins Server

In this lesson, you’ll deploy an internet-accessible Jenkins server using AWS CloudFormation and complete the initial Jenkins setup.

This approach allows you to provision all required infrastructure and software with minimal manual configuration.

The full process takes about **10–15 minutes**, including stack deployment time.

## **Overview**

In this exercise, you will:

1. Deploy a Jenkins server using a prebuilt CloudFormation template.
2. Wait for AWS to provision and configure the server.
3. Retrieve the Jenkins initial admin password.
4. Complete the Jenkins first-time setup through the web interface.

Once complete, your Jenkins server will be ready for use in the rest of the course.

## **Instructions**

### **Create the CloudFormation Stack**

1. Log in to your **AWS Management Console**.

2. Navigate to **CloudFormation**.

3. Select **Create stack**, then choose **With new resources (standard)**.

4. On the **Specify template** screen:

   - Select **Upload a template file**.
   - Select **Choose file**.

5. From the exercise files, select the CloudFormation template that deploys the Jenkins server: [`jenkins-server-cloudformation-template.yml`](./jenkins-server-cloudformation-template.yml)

6. Select **Next**.

### **Configure Stack Details**

1. On the **Specify stack details** screen, enter a stack name: `jenkins-server`

2. Leave the **InstanceType** parameter set to the default value.

3. Select **Next**.

### **Configure Stack Options**

1. On the **Configure stack options** screen:

   - Leave all options set to their default values.
   - Scroll to the bottom of the page.

2. Acknowledge that CloudFormation may create IAM resources.

3. Select **Next**.

### **Review and Submit**

1. On the **Review** screen:

   - Scroll to the bottom.
   - Review the configuration if desired.

2. Select **Submit**.

### **Wait for Stack Deployment**

1. Wait for the CloudFormation stack status to change to **CREATE_COMPLETE**.

> [!TIP]
> This process typically takes **about five minutes**.

### **Review Stack Outputs**

1. Once the stack has deployed successfully, select the **Outputs** tab.

2. Review the values provided:

   - **InitialAdminPassword** – A command used to retrieve the Jenkins admin password.
   - **JenkinsURL** – The public URL for accessing Jenkins.
   - **TerminalURL** – A link to open a terminal session on the server using AWS Systems Manager.

### **Retrieve the Initial Admin Password**

1. Copy the command shown in the **InitialAdminPassword** output: `sudo cat /var/lib/jenkins/secrets/initialAdminPassword`

2. Open the link next to **TerminalURL** in a new browser tab.

3. In the terminal session, paste the command and run it.

4. Copy the password displayed in the terminal.

### **Access Jenkins**

1. Open the link next to **JenkinsURL** in a new browser tab.

2. On the **Unlock Jenkins** screen:

   - Paste the initial admin password.
   - Select **Continue**.

### **Install Plugins and Create Admin User**

1. On the plugin selection screen, select **Install selected plugins**.

2. Wait for the plugin installation to complete.

3. When prompted, create the first admin user:

   - Enter a username.
   - Enter and confirm a password.
   - Enter a full name and email address.

4. Select **Save and Continue**.

### **Finalize Setup**

1. On the instance configuration screen, keep the default settings.  Select **SAVE AND FINISH**

2. Select **Start using Jenkins**.

## **Next Steps**

Your Jenkins server is now deployed and fully configured.

Move on to the next lesson and begin working with Jenkins pipelines.

<!-- FooterStart -->
---
[← 00_01 From Code to Production With Jenkins](../00_01_from_code_to_production_with_jenkins/README.md) | [01_01 Create a Pipeline Project →](../../ch1_the_jenkins_pipeline/01_01_create_a_pipeline_project/README.md)
<!-- FooterEnd -->
