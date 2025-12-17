# 05_03 Use Secrets and Credentials

Jenkins can store and manage sensitive values natively.

In Jenkins, sensitive values are referred to as **secrets** or **credentials**.
In this course, both terms are used interchangeably.

## Types of Credentials

Jenkins supports several credential types, including:

- **Username and password**
- **SSH keys**
- **Files**
- **Secret text (strings)**

## Using Credentials in Pipelines

Credentials can be accessed in multiple ways, but the two most common are:

- The `credentials()` function
- The `withCredentials {}` build step

## `credentials()` - Assign to environment variables globally

The `credentials()` function assigns a stored secret to environment variables.
It takes the **credential ID** as its argument.

- Most credentials return a **single value**:

    ```groovy
    environment {
        SECRET_VALUE = credentials('secret-value')
    }
    ```

- Access the value with:

    ```groovy
    env.SECRET_VALUE
    ```

- Username/password credentials return **three variables**:

    With the `login` credential saved as a username:password type, the following assignment to `LOGIN`...

    ```groovy
    environment {
        LOGIN = credentials('login')
    }
    ```

- Would create the following variables:

    ```groovy
    env.LOGIN
    env.LOGIN_USR
    env.LOGIN_PSW
    ```

## `withCredentials {}` — Assign to environment variable locally

`withCredentials {}` is a build step that retrieves a credential and assigns it to a variable.

- Credentials are only available **inside the block**
- Only **Secret Text** credentials can be used with `withCredentials`

    ```groovy
    steps {
        withCredentials([string(credentialsId: 'apikey', variable: 'API_KEY')]) {
            echo "${env.API_KEY}"
        }
    }
    ```

## Quick Comparison

| Method| Scope| Common Use Case|
| -------------------- | ------------------------ | -------------------- |
| `credentials()`| Entire pipeline or stage | Environment variables needed across steps |
| `withCredentials {}` | Limited block | Minimize exposure of sensitive values |

## Best Practices

- Never hard-code secrets in Jenkinsfiles
- Use the **smallest scope possible** for secrets
- Prefer `withCredentials {}` when a value is only needed briefly, ie for a single step

## Lab: Creating and Using Jenkins Credentials in a Pipeline

In this lab, you'll create Jenkins credentials and use them securely inside a pipeline. You'll work with two credential types and see how Jenkins protects sensitive values in the build output.

### Prerequisites

Before starting this lab, make sure you have:

- A running Jenkins server
- Administrative access to Jenkins
- The exercise files for this lesson

### Part 1: Create Jenkins Credentials

#### 1. Open the Credentials Manager

1. From the Jenkins dashboard, select **Manage Jenkins**
2. Select **Credentials**

This page lists all existing credentials and the domains where Jenkins can store and access them.

#### 2. Select the Global Domain

1. Select **(global)** from the list of available domains

The global domain makes credentials available to all jobs on the Jenkins server.

#### 3. Create a Secret Text Credential

1. Select **Add Credentials**

2. From the **Kind** dropdown, review the available credential types

3. Select **Secret Text**

4. Leave the **Scope** set to **Global**

5. In the **Secret** field, enter any placeholder value (for example: `my-api-key`)

6. In the **ID** field, enter:

   ```text
   apikey
   ```

7. In the **Description** field, enter:

   ```text
   This is the API key for the Amazing online service
   ```

8. Select **Create**

#### 4. Create a Username and Password Credential

1. Select **Add Credentials**
2. From the **Kind** dropdown, select **Username with password**
3. Enter any placeholder values for:

   - **Username**
   - **Password**

4. Set the **ID** to:

   ```text
   login
   ```

5. Select **Create**

You should now have two credentials:

- A **Secret Text** credential with ID `apikey`
- A **Username and Password** credential with ID `login`

### Part 2: Use Credentials in a Pipeline

#### 1. Create a Pipeline Job

Create a **Pipeline** job using the [Jenkinsfile](./Jenkinsfile) included with this lesson.

#### 2. Review the Jenkinsfile

Open the pipeline configuration and review how credentials are used.

#### Using `credentials()` in the environment block

```groovy
environment {
    LOGIN = credentials('login')
}
```

This pulls the username and password from the `login` credential and assigns them to environment variables.

#### Using `withCredentials {}` in a build step

```groovy
withCredentials([string(credentialsId: 'apikey', variable: 'APIKEY')]) {
    ...
}
```

This retrieves the `apikey` secret text credential and makes it available only within the block.

#### 3. Save and Run the Pipeline

1. Select **Save**
2. Select **Build Now**
3. Open the most recent build
4. Navigate to **Pipeline Overview**
5. Open the console output for each build step

### Part 3: Review the Results

As you review the console output, notice the following:

- The values for `APIKEY`, `LOGIN`, and `LOGIN_PSW` are **masked**
- Jenkins prevents secrets from being displayed in plain text
- A warning appears when a credential is passed directly to an output

This is Jenkins actively protecting sensitive information in your pipeline.

<!-- FooterStart -->
---
[← 05_02 Configure Project-Based Permissions](../05_02_configure_projectbased_permissions/README.md) | [05_04 Challenge: Configure Users and Permissions →](../05_04_challenge_configure_users_permissions/README.md)
<!-- FooterEnd -->
