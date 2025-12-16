# 04_02 Publish Test Results and Code Coverage Reports

Testing is a core part of any Continuous Integration (CI) pipeline.  Tests help teams identify bugs early—long before code reaches production.  Early detection reduces risk, speeds up feedback, and improves overall code quality.

## Testing in the CI Pipeline

Typical CI pipeline flow:

```bash
Lint → Test → Build → Deploy
```

- **Lint**: Checks code style and basic issues.
- **Test**: Executes automated tests and generates reports.
- **Build**: Packages the application.
- **Deploy**: Releases the application to an environment.

## Test Reports

### JUnit Reports

- JUnit reports are **XML files** that describe test results.
- Originally created for Java testing.
- Widely adopted by many other programming languages.
- Considered the **standard format** for test reporting.

### JUnit Plugin

- <https://plugins.jenkins.io/junit/>
- Collects JUnit-format test reports.
- Publishes test results as graphs.
- Tracks trends such as:

  - Test pass/fail rates
  - Stability over time
  - Regressions across builds

## Code Coverage

- Measures which lines of code are executed during tests.
- Helps determine how thoroughly the application is tested.
- Higher coverage generally increases the likelihood of finding bugs.

### Common Code Coverage Formats

- **JaCoCo**
- **Cobertura**

> [!NOTE]
> The JUnit, JaCoCo, and Cobertura report formats originated in the Java ecosystem. Many non-Java tools also generate reports using these formats due to their popularity.

### Coverage Plugin

- <https://plugins.jenkins.io/coverage/>
- Collects and publishes multiple code coverage report formats.
- Supports JaCoCo, Cobertura, and others.
- Visualizes coverage metrics and trends across builds.

## Lab: Get Hands-On With Test and Code Coverage Reports

In this lab, you'll create a Jenkins pipeline job named `publish-reports`. The pipeline checks out a Python project, installs dependencies, runs linting and tests, and generates two types of reports:

- Test report in **JUnit** format
- Code coverage reports in **Cobertura** format

Jenkins will process these reports in the `post` section of the pipeline, publish visual trends, and archive the reports as build artifacts.

### Prerequisites

Before starting this lab, make sure you have:

- A running Jenkins server
- The exercise files for this lesson
- The following Jenkins plugins installed:

  - **JUnit Plugin**
  - **Coverage Plugin**

> [!IMPORTANT]
> If the Coverage Plugin is not installed, the pipeline will fail during the coverage collection step.

### Instructions

#### 1. Create the Pipeline Job

1. From the Jenkins dashboard, select **New Item**.
2. Enter the job name `publish-reports`.
3. Select **Pipeline** as the job type.
4. Select **OK**.

#### 2. Configure the Pipeline

1. In the job configuration screen, scroll to the **Pipeline** section.
2. Configure the pipeline to use the provided [`Jenkinsfile`](./Jenkinsfile) from the exercise files.
3. Save the job configuration.

#### 3. Review the Pipeline Stages

1. Open the `publish-reports` pipeline job.

2. Review the early setup stages and note that they:

   - Check out the source code
   - Install Python dependencies
   - Lint the code for syntax and style issues

3. Review the **Test** stage.

   - This stage runs the test suite.
   - It generates:

     - A **JUnit XML** test report
     - A **Cobertura XML** code coverage report

4. The **Build** and **Deploy** stages are place holders for now.

#### 4. Review the Post Section

1. Review the `post` block in the pipeline definition.
2. Observe that this section:

   - Processes the JUnit test report
   - Processes the Cobertura coverage report
   - Archives the reports as build artifacts

The `post` section runs after all pipeline stages, ensuring reports are collected even if earlier stages fail.

#### 5. Run the Pipeline

1. Return to the `publish-reports` job and select **Build Now**.
2. Wait for the pipeline to complete successfully.

#### 6. View Test and Coverage Trends

1. On the `publish-reports` job home page, locate the graphs on the right side of the screen.
2. Identify:

   - The **Test Results Trend** graph
   - The **Code Coverage Trend** graph

These graphs show how test results and coverage change over time across builds.

#### 7. Explore the Coverage Report

1. From the job menu on the left, select **Coverage Report**.

2. Select **Overview** if it is not already selected.

   - Review coverage summarized by line, class, and file.

3. Select the **Files** tab.

   - Review coverage results for individual files.

4. Select **app.py**.

   - Review line-by-line coverage information for the file.

#### 9. Explore the Test Results

1. From the job menu on the left, select **Tests**.

2. Review the summary of:

   - Passed tests
   - Failed tests
   - Skipped tests

3. Select the **test_app** package.

4. Select **Tests**.

   - Review the individual test cases and their results.

All tests should be passing in the completed pipeline run.

### Next Steps

In the next lesson, you’ll go a step further by using test results to control how a pipeline behaves.

<!-- FooterStart -->
---
[← 04_01 Artifacts and Fingerprinting](../04_01_artifacts_fingerprinting/README.md) | [04_03 Use Test Results to Stop a Pipeline →](../04_03_use_test_results/README.md)
<!-- FooterEnd -->
