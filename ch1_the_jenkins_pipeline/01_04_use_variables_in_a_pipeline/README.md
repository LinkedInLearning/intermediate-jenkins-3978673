# 01_04 Use Variables In a Pipeline

The most commonly used variables are **environment variables** and **parameters**.

Variables let us use dynamic values in pipelines.

This lesson will focuses on environment variables. We'll use another lesson to discuss parameters.

## Environment variables

Environment variables can be set globally for an entire pipeline. Or they can be set locally in a stage.

## Global Variables Reference

You can find documentation for global variables by starting on the homepage for a pipeline job and then viewing:

- `Pipeline Syntax` &rarr; `Global Variables Reference`

## Scoping Variables Globally and Locally

Use the following pipeline to see a demonstration of how environment variables can be scoped globally (for the entire pipeline) or locally for a single step.

```Jenkinsfile
pipeline {
    agent any
    environment {
        MAX_SIZE = 10
        MIN_SIZE = 1
    }
    stages {
        stage('Default Scale') {
            steps {
                echo "MAX_SIZE = ${env.MAX_SIZE}"
                echo "MIN_SIZE = ${env.MIN_SIZE}"
            }
        }
        stage('Scale by 10x') {
            environment {
                MAX_SIZE = 100
                MIN_SIZE = 10
            }
            steps {
                echo "MAX_SIZE = ${env.MAX_SIZE}"
                echo "MIN_SIZE = ${env.MIN_SIZE}"
            }
        }
    }
}
```

## Shenanigans: Current Build Variables

There's one more type of variable you can use but it wasn't discussed in the video lecture: **current build variables**.

Current build variables allow pipeline steps to reference the state of a build while it's running.

This can be useful for dynamic operations that need to do something specific based on a previous step or a certain status in the build.

All of the current build variables are actually properties of one variable named `currentBuild`.  Please note that this variable is case sensitive and written in [camel case](https://en.wikipedia.org/wiki/Camel_case); it starts with a lower case **c** and the **B** is capitalized.

To access the currentBuild properties, the values are preceded by `currentBuild`, a dot, and then the name of the property.  The properties are also case sensitive and follow the camel case format.

A few examples of current build variables are the start time, the duration of the build, and the current status of the build.

```
currentBuild.duration
currentBuild.startTimeInMillis
currentBuild.currentResult
```

Just like environment variables, these values need to be preceded by a dollar sign if they’re used in strings.

## Bonus Shenanigans: Print "most" of the default global variables

View the following file for a bonus pipeline that prints "most" of the global variables _and_ some current build variables too!

[PIPELINE_WITH_MOST_VARIABLES](PIPELINE_WITH_MOST_VARIABLES.md)

<!-- FooterStart -->
---
[← 01_03 Use the Pipeline Snippet Generator](../01_03_use_the_pipeline_snippet_generator/README.md) | [01_05 Parameterize a Pipeline →](../01_05_parameterize_a_pipeline/README.md)
<!-- FooterEnd -->
