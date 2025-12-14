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

<!-- FooterStart -->
---
[← 04_01 Artifacts and Fingerprinting](../04_01_artifacts_fingerprinting/README.md) | [04_03 Use Test Results to Stop a Build →](../04_03_use_test_results_to_stop_a_build/README.md)
<!-- FooterEnd -->
