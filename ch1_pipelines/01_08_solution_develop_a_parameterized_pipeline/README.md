# 01_08 Solution: Develop a Parameterized Pipeline

In this challenge, you’ll update an existing Jenkins pipeline so that it accepts **parameters** and behaves differently based on user input. You’ll add pipeline parameters, apply conditional logic to control deployments, and generate reports using values provided at runtime.

By the end of this challenge, you’ll have hands-on experience working with **parameterized declarative pipelines**, conditional execution, and artifact generation in Jenkins.

## Challenge Tasks

To complete this challenge, you will:

- Create a new Jenkins pipeline job
- Add parameters to a declarative Jenkins pipeline
- Restrict deployment behavior based on parameter values
- Use parameter values inside pipeline steps
- Generate and archive a parameterized report artifact

This challenge should take **15–20 minutes** to complete.

## Prerequisites

Before you begin, make sure you have:

- Access to a running Jenkins server
- Familiarity with editing a `Jenkinsfile`

## Instructions

### Step 1: Create a New Pipeline Job

1. Log in to your Jenkins server.
2. From the Jenkins dashboard, select **New Item**.
3. Enter a name for the pipeline job.
4. Select **Pipeline** as the job type.
5. Select **OK** to create the job.

### Step 2: Add the Starter Pipeline Code

1. In the pipeline configuration screen, scroll to the **Pipeline** section.
2. Set **Definition** to **Pipeline script**.
3. Paste the following starter pipeline code into the script editor:

    ```groovy
    pipeline {
        agent any
        stages {
            stage('Test') {
                steps {
                    echo "This step tests the project"
                }
            }
            stage('Deploy') {
                steps {
                    echo "This stage deploys the project"
                }
            }
            stage('Report') {
                steps {
                    echo "This stage generates a report"
                    sh 'printf "This is the change log." > report.txt'
                    archiveArtifacts allowEmptyArchive: true,
                        artifacts: '*.txt',
                        fingerprint: true,
                        followSymlinks: false,
                        onlyIfSuccessful: true
                }
            }
        }
    }
    ```

4. Select **Save**.

### Step 3: Add Pipeline Parameters

Update the pipeline to include the following parameters:

| Parameter Name | Type | Description | Default Value |
|----------------|------|-------------|---------------|
| `ENVIRONMENT` | Choice | Selects the deployment environment | `DEVELOPMENT` |
| `API_KEY` | Password | API key used during deployment | `123ABC` |
| `CHANGELOG` | Text | Notes describing the changes in this build | `This is the change log.` |

**Requirements:**

- `ENVIRONMENT` must allow:

  - `DEVELOPMENT`
  - `STAGING`
  - `PRODUCTION`

- Parameters must be defined using the declarative `parameters` block.

> [!TIP]
> You can use the **Declarative Directive Generator** in Jenkins to help build parameter syntax.

### Step 4: Restrict the Deploy Stage

Update the **Deploy** stage so that it only runs when:

- `ENVIRONMENT` is set to `PRODUCTION`

**Expected behavior:**

- Deploy runs for production builds
- Deploy is skipped for development and staging builds

### Step 5: Parameterize the Report Stage

Update the **Report** stage to:

1. Use the value of `CHANGELOG` as the report content.
2. Name the report file using the selected environment.

**Example:**

- If `ENVIRONMENT` is `STAGING`, the report file should be:

    ```bash
    STAGING.txt
    ```

The report must still be archived as a build artifact.

### Step 6: Run and Verify the Pipeline

1. Select **Build with Parameters**.
2. Run the pipeline multiple times using different environment values.
3. Verify the following behavior:

- The **Deploy** stage only runs for production builds
- The report file:

  - Uses the selected environment as its filename
  - Contains the changelog text entered at build time

- The report artifact is available after a successful build

## Challenge Completion

- Confirm all required parameters are present
- Verify conditional deployment logic works correctly
- Verify reports are generated and archived as expected

Compare your implementation to the following solution:

```groovy
pipeline {
    agent any
    parameters {
      choice choices: ['DEVELOPMENT', 'STAGING', 'PRODUCTION'],
         description: 'Choose the environment for this deployment.',
         name: 'ENVIRONMENT'

      password defaultValue: '123ABC',
         description: 'Enter the API key to use for this deployment.',
         name: 'API_KEY'

      text defaultValue: 'This is the change log.',
         description: 'Enter the components that were changed in this deployment.',
         name: 'CHANGELOG'
    }
    stages {
        stage('Test') {
            steps {
                echo "This step tests the compiled project"
            }
        }
        stage('Deploy') {
            when {
              expression { params.ENVIRONMENT == "PRODUCTION" }
            }
            steps {
                echo "This step deploys the project"
            }
        }
        stage('Report') {
            steps {
                echo "This stage generates a report"
                sh "printf \"${params.CHANGELOG}\" > ${params.ENVIRONMENT}.txt"
                archiveArtifacts allowEmptyArchive: true,
                    artifacts: '*.txt',
                    fingerprint: true,
                    followSymlinks: false,
                    onlyIfSuccessful: true
            }
        }
    }
}
```

### Optional Reflection

1. When would you use parameters instead of environment variables?

When you’re ready, move on to the next chapter!

<!-- FooterStart -->
---
[← 01_07 Challenge: Develop a Parameterized Pipeline](../01_07_challenge_develop_a_parameterized_pipeline/README.md) | [02_01 Pipeline as Code With Jenkinsfile →](../../ch2_version_control_systems/02_01_pipeline_as_code_with_jenkinsfile/README.md)
<!-- FooterEnd -->
