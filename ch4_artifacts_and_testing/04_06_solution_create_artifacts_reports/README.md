# 04_06 Solution: Create artifacts and Reports

In this challenge, you’ll configure Jenkins to run a Maven-based build, publish JUnit test results, and archive the build artifact so it’s available after the job finishes.

## Challenge Tasks

To complete this challenge, you will:

- Set up a global tool configuration for Maven.
- Make sure the JUnit plugin is installed.
- Update the pipeline to use the Maven tool configuration.
- Update the pipeline to call Maven.
- Update the pipeline to collect test results and archive artifacts from the project workspace

This challenge should take **15–20 minutes** to complete.

## Prerequisites

Before you begin, make sure you have:

- Access to a running Jenkins server
- Familiarity with editing a `Jenkinsfile`

## Instructions

### Step 1: Create a new pipeline job

1. Log in to your Jenkins server.
2. From the Jenkins dashboard, select **New Item**.
3. Enter a name for the pipeline job.
4. Select **Pipeline** as the job type.
5. Select **OK** to create the job.

### Step 2: Add the Starter Pipeline Code

1. In the pipeline configuration screen, scroll to the **Pipeline** section.
2. Set **Definition** to **Pipeline script**.
3. Add the provided [Jenkinsfile](./Jenkinsfile) into the script editor.
4. Select **Save**.

### Step 3: Configure Maven and the JUnit plugin

1. From the Jenkins dashboard, select the cog icon for **Manage Jenkins**.
2. Select **Tools**.
3. Scroll to the **Maven installations** section.
4. Select **Add Maven**.
5. In **Name**, enter `maven-3.9.12`.
6. Select **Install automatically**.
7. For **Version**, select **3.9.12**.
8. Select **Save**.
9. Select **Plugins**.
10. Select **Installed plugins**.
11. Search for `JUnit Plugin`.
12. Confirm **JUnit Plugin** appears in the list of installed plugins. \_Note: If the plugin is not installed, select **Available plugins**, search for `JUnit Plugin`, install the plugin, and then restart Jenkins if prompted.

### Step 4: Update the pipeline to use Maven and archive artifacts

1. Open your pipeline job and select **Configure**.
2. Scroll to the **Pipeline** section and locate the script editor.
3. Add the Maven tool configuration near the top of the pipeline (below `agent any`) so Jenkins provides Maven to the build.  Add a `tools` block that references the Maven installer name `maven-3.9.12`.
4. In each stage (`Clean`, `Test`, and `Package`), uncomment the Maven commands so the pipeline actually runs the build.
5. In the `post { always { ... } }` section, replace the placeholder comments with steps that publish test results and archive the JAR file.
6. Add a `junit` step that collects the test report file: `**/TEST-com.learningjenkins.AppTest.xml`
7. Add an `archiveArtifacts` step that archives the JAR file: `**/hello-1.0-SNAPSHOT.jar`
8. Select **Save** to apply your changes.

## Challenge Completion

1. **Confirm** the pipeline runs successfully from start to finish by selecting **Build Now** and verifying all stages complete without errors.
2. Open the completed build and
   - confirm **Test Result** is available.
   - confirm the archived artifact includes `hello-1.0-SNAPSHOT.jar`.

Compare your implementation to the solution: [Jenkinsfile](./Jenkinsfile).

<!-- FooterStart -->
---
[← 04_05 Challenge: Create artifacts and Reports](../04_05_challenge_create_artifacts_reports/README.md) | [05_01 Secure Jenkins With User accounts →](../../ch5_securing_jenkins/05_01_secure_jenkins_with_user_accounts/README.md)
<!-- FooterEnd -->
