# 01_05 Parameterize a Pipeline

Parameters are defined in a `parameters` block which is placed at the beginning of the pipeline code.

```Jenkinsfile
pipeline {
    agent any
    parameters {
       …
    }
    …
}
```

Parameters are accessed by their name preceded by the `params` prefix.

If they’re used in a string, they need to have a dollar sign at the beginning with the `params` prefix and the variable name wrapped in curly braces.

```Jenkinsfile
params.PARAMETER_NAME
"${params.PARAMETER_NAME}"
```

## Declaring parameters

For pipelines, there are five different types of parameters we can use:

| Parameter | Description                                      |
|-----------|--------------------------------------------------|
| string    | A single line of text.                           |
| text      | Multiple lines of text.                          |
| boolean   | A true/false checkbox.                           |
| choice    | A dropdown list of options.                      |
| password  | A masked text field for sensitive data.          |

Each parameter definition must include a name, a default value, and a description that explains the type of value that should be entered.

## Sample pipeline with parameters

Use the following pipeline script to experiment with parameters.

```Jenkinsfile
pipeline {
    agent any
    parameters {
        string(name: 'FATHER',
               defaultValue: 'Vader',
               description: 'Enter Your father’s name')

        text(name: 'PHRASE',
                description: 'Enter your favorite phrase from a Charles Dickens Book',
                defaultValue: 'It was the best of times, it was the worst of times,\nit was the age of wisdom, it was the age of foolishness,\nit was the epoch of belief, it was the epoch of incredulity,\nit was the season of light, it was the season of darkness,\nit was the spring of hope, it was the winter of despair.')

        booleanParam(name: 'RUN_TESTS',
                defaultValue: false,
                description: 'Toggle this value to run tests.')

        choice(name: 'AWS_REGION',
                choices: ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'],
                description: 'Select the AWS region for deployment.')

        password(name: 'DATABASE_PASSWORD',
                defaultValue: 'DATABASE_PASSWORD',
                description: 'Enter the database password')
    }
    stages {
        stage('Example') {
            steps {
                echo "I am your father.  My name is ${params.FATHER}"
                echo "My favorite phrase is ${params.PHRASE}"
                echo "Will I rule the universe? ${params.RUN_TESTS}"
                echo "I live in ${params.AWS_REGION}"
                echo "Can I tell you a secret? ${params.DATABASE_PASSWORD}"
            }
        }
    }
}
```

<!-- FooterStart -->
---
[← 01_04 Use Variables In a Pipeline](../01_04_use_variables_in_a_pipeline/README.md) | [01_06 Use Conditional Expressions and Manual approvals →](../01_06_use_conditional_expressions_manual_approvals/README.md)
<!-- FooterEnd -->
