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
    // agent { dockerContainer 'maven:latest' }
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
                sh 'ls -ltr > report.txt'
                git url: 'https://github.com/octocat/Hello-World.git'
            }
        }
    }
}
```

## Pipeline References

### Basic Steps

For the complete list of basic steps, take a look at the **basic steps reference** in the Jenkins documentation. In this list, you'll find dozens of steps available for use in a pipeline.

- [Basic Pipeline Steps](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/)

### Steps Provided by Extensions

As you install plug-ins or extend the functionality of your Jenkins server, you'll find that many plugins expose their own pipeline steps.

For more information on these additional steps, take a look at the **Pipeline Steps Reference** in the Jenkins documentation.

There are literally hundreds of steps to choose from. so I Review the list to see if there are any tools that you're already using that can be called from a pipeline step.

- [Steps Provided by Extensions](https://www.jenkins.io/doc/pipeline/steps/)

<!-- FooterStart -->
---
[← 01_01 Create a Pipeline Project](../01_01_create_a_pipeline_project/README.md) | [01_03 Use the Pipeline Snippet Generator →](../01_03_use_the_pipeline_snippet_generator/README.md)
<!-- FooterEnd -->
