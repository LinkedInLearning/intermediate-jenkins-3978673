# 01_02 Use Build Steps in a Pipeline

Jenkins pipelines start with the word `pipeline` followed by curly braces and configuration details.

## Required sections in the pipeline configuration

A pipeline configuration has three required sections.

- `agent`
- `stages`
- at least one `stage` and at least one `step`

## Using Build Steps

Create a pipeline job and paste in the following pipeline configuration.

Run the job and examine the output.

```Jenkinsfile
pipeline {
    agent any
    // agent { label ‘windows-11’ }
    // agent { docker { image 'maven:3.9-amazoncorretto-17-debian' } }
    // agent none
    stages {
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
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('More Steps') {
            steps {
                echo 'More steps to use...'
                sh 'ls -ltr'
                git url: 'https://github.com/octocat/Hello-World.git'
                archiveArtifacts artifacts: 'README'
            }
        }
    }
}
```

<!-- FooterStart -->
---
[← 01_01 Create a Pipeline Project](../01_01_create_a_pipeline_project/README.md) | [01_03 Use the Pipeline Snippet Generator →](../01_03_use_the_pipeline_snippet_generator/README.md)
<!-- FooterEnd -->
