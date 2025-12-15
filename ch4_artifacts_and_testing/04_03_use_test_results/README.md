# 04_03 Use Test Results to Stop a Pipeline

In this lesson, you'll create two Jenkins pipeline jobs:

- `publish-reports-pipeline-fail`
- `publish-reports-pipeline-unstable`

The goal is to compare the results of these pipelines and understand how Jenkins handles test failures by default versus how pipeline behavior changes when failures are explicitly handled.

## Prerequisites

Before starting, make sure you have:

- A running Jenkins server
- The exercise files for this lesson
- The following Jenkins plugins installed:

  - **JUnit Plugin**
  - **Coverage Plugin**

> [!IMPORTANT]
> If the Coverage Plugin is not installed, the pipeline will fail during the coverage collection step.

## Instructions

### 1. Review the failing tests

This lesson uses a test file that is intentionally designed to fail every time.

- Open the test file included in the exercise files:
  [`test_always_fail.py`](./test_always_fail.py)

As you review the file, note that the assertions are written so the test suite will always fail, regardless of input or environment. This predictable failure allows you to clearly observe how Jenkins responds to test failures under different pipeline configurations.

### 2. Create the pipeline jobs

Create two pipeline jobs using Jenkinsfiles provided in the exercise files.

1. Create a new **Pipeline** job named `publish-reports-pipeline-fail`.

   - Use the following pipeline configuration:
     [`publish-reports-pipeline-fail.Jenkinsfile`](./publish-reports-pipeline-fail.Jenkinsfile)

2. Create a second **Pipeline** job named `publish-reports-pipeline-unstable`.

   - Use the following pipeline configuration:
     [`publish-reports-pipeline-unstable.Jenkinsfile`](./publish-reports-pipeline-unstable.Jenkinsfile)

Both pipelines use the same stages and test suite. The key difference between them appears in how the `Test` stage is implemented.

### 3. Review and compare the `Test` stage in both pipelines

Before running the pipelines, review the `Test` stage in each Jenkinsfile.

- In the **failed pipeline**, the `pytest` and code coverage commands run normally. When the tests fail, Jenkins treats the failure as fatal for the pipeline.
- In the **unstable pipeline**, the `pytest` and coverage commands are wrapped with the `catchError` directive.

The `catchError` directive allows Jenkins to:

- Capture errors from the test and coverage steps
- Mark the *stage* as failed
- Mark the *overall build* as **UNSTABLE** instead of **FAILED**

This configuration signals that something went wrong, while still allowing later stages in the pipeline to run.

Read the [`catchError` documentation](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#catcherror-catch-error-and-set-build-result-to-failure) for more details.

### 4. Run both pipelines and compare the results

Run each pipeline and observe the results.

1. Run `publish-reports-pipeline-fail`.

   - Review the pipeline overview.
   - Note that the failure occurs in the `Test` stage.
   - Observe that the **Build** and **Deploy** stages are skipped.
   - The pipeline finishes with a **FAILED** status.

2. Run `publish-reports-pipeline-unstable`.

   - Review the pipeline overview.
   - Note that the `Test` stage still fails.
   - Observe that the **Build** and **Deploy** stages are allowed to run and complete.
   - The pipeline finishes with an **UNSTABLE** status.

Compare the status indicators in Jenkins:

- A red ❌ indicates a failed pipeline.
- An orange ⚠️ indicates an unstable pipeline.

This comparison highlights how test failures can either stop a pipeline entirely or allow it to continue, depending on how errors are handled.

## Next Steps

In the next lesson, you’ll install and configure a Jenkins plugin that uses AI-assisted analysis to explain test failures and other pipeline errors, making it easier to diagnose issues directly from Jenkins build results.

<!-- FooterStart -->
---
[← 04_02 Publish Test Results and Code Coverage Reports](../04_02_publish_reports/README.md) | [04_04 TBD: Use an External Test Runner and/Or AI tool →](../04_04_tbd_use_an_external_test_runner_or_ai_tool/README.md)
<!-- FooterEnd -->
