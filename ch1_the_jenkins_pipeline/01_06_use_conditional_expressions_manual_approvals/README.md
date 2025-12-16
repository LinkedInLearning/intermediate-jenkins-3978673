# 01_06 Use Conditional Expressions and Manual approvals

When we’re developing pipelines, we might need to use logic to determine if a stage should be run or not.  We might also need to add some sort of manual interaction to an automated process.

## Conditionals

To set up a pipeline condition, we use the `when` keyword inside a stage block.

```Jenkinsfile
pipeline {
   agent any
   stages {
      stage('XYZ') {
         when {}
      }
   }
}
```

A `when` block can use three built-in conditions to determine if the the steps in a stage should be run.  The conditions are:

|Condition  |Syntax                                                       |
|:----------|:------------------------------------------------------------|
|branch     |`when { branch 'main' }`                                     |
|environment|`when { environment name: 'RELEASE_DAY', value: 'FRIDAY' }`  |
|expression |`when { expression { params.DEPLOY_TARGET == 'PRODUCTION' }}`|

Expression conditions provide the most flexibility for conditional statements.  We can use Groovy expressions along with parameters and other variables to build a statement that returns true or false.

Review the following document for more information on Groovy expressions:

- [The Apache Groovy programming language - Operators](https://groovy-lang.org/operators.html)

## Manual Approvals

The input step pauses a triggered pipeline and waits for manual interaction to determine if the pipeline should proceed or abort.

```Jenkinsfile
pipeline {
   agent any
   stages {
      stage('XYZ') {
         steps {
            input message: 'Confirm deployment to production...', ok: 'Deploy'
         }
      }
   }
}
```

Review the following document for more information on the `input` step:

- [Pipeline: Input Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/)

## Example using conditional and manual approval

Use the following pipeline script in a new project to experiment with conditionals and manual approvals.

```Jenkinsfile
pipeline {
    agent any
    environment {
        RELEASE_DAY = 'FRIDAY'
    }
    parameters {
        choice(
            name: 'DEPLOY_TARGET',
            choices: ['DEVELOPMENT', 'STAGING', 'PRODUCTION'],
            description: 'Choose the target environment for this deployment'
        )
    }

    stages {
        // Branch-based conditional
        stage('Run tests on main branch') {
            when {
                // This stage only runs when the pipeline is triggered from the 'main' branch
                branch 'main'
            }
            steps {
                echo "Running tests for the 'main' branch."
            }
        }

        // Environment-variable-based conditional
        stage('Environment-based tasks') {
            when {
                // This stage runs only if the RELEASE_DAY environment variable equals 'FRIDAY'
                environment name: 'RELEASE_DAY', value: 'FRIDAY'
            }
            steps {
                echo "echo Deploying on a Friday? Nice. 😎"
            }
        }

        // Expression-based conditional
        stage('Deploy to non-production environment') {
            when {
                // Only deploy automatically when the target is NOT production
                expression {
                    params.DEPLOY_TARGET != 'PRODUCTION' && (env.RELEASE_DAY == 'FRIDAY' || env.RELEASE_DAY != 'FRIDAY')
                }
            }
            steps {
                echo "Auto-deploying to ${params.DEPLOY_TARGET} (no manual approval required)."
            }
        }

        // Manual approval
        stage('Deploy to production') {
            when {
                // Only run this stage when the target is PRODUCTION
                expression { params.DEPLOY_TARGET == 'PRODUCTION' }
            }
            steps {
                // Manual approval before proceeding with production deployment
                input message: 'You are about to deploy to PRODUCTION. Do you want to continue?', ok: 'Deploy'
                echo "Deploying to ${params.DEPLOY_TARGET} with manual approval."
            }
        }
    }
}
```

<!-- FooterStart -->
---
[← 01_05 Parameterize a Pipeline](../01_05_parameterize_a_pipeline/README.md) | [01_07 Challenge: Develop a Parameterized Pipeline →](../01_07_challenge_develop_a_parameterized_pipeline/README.md)
<!-- FooterEnd -->
