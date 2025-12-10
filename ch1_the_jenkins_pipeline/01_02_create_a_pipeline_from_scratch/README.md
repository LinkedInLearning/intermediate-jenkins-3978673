# 01_02 Create a Pipeline From Scratch

Jenkins pipelines start with the word `pipeline` followed by curly braces and configuration details.

## Required sections in the pipeline configuration

A pipeline configuration has three required sections.

- `agent`
- `stages`
- at least one `stage` and at least one `step`

## A multi-stage pipeline

Create a pipeline job and paste in the following code to create a multi-stage pipeline.

Run the job and examine the output.

```Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Requirements') {
            steps {
                echo 'Getting Requirements....'
            }
        }
        stage('Build') {
            steps {
                echo 'Building....'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..1'
                echo 'Testing..2'
                echo 'Testing..3'
            }
        }
        stage('Report') {
            steps {
                echo 'Reporting....'
            }
        }
    }
}
```

<!-- FooterStart -->
---
[← 01_01 Create a Pipeline Project](../01_01_create_a_pipeline_project/README.md) | [01_03 Use the Pipeline Snippet Generator →](../01_03_use_the_pipeline_snippet_generator/README.md)
<!-- FooterEnd -->
