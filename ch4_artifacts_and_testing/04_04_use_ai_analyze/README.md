# 04_04 Use AI to Analyze Errors

In this lab, you’ll use an AI-enabled Jenkins plugin to analyze a failed pipeline and turn a difficult-to-interpret error into clear, actionable guidance.

The goal is to use AI as a **diagnostic aid**—helping you understand *why* a job failed and *where* to focus your attention when debugging unfamiliar or navigating complex errors.

## Prerequisites

Before starting this lab, make sure you have:

- A running Jenkins server (Jenkins 2.479.3 or newer)
- Java 21 or newer installed on the Jenkins server
- The exercise files for this lesson
- Permission to use AI tools in your organization

> [!CAUTION]
> The use of AI tools for software development may be subject to company or organizational policies.
> Before using the Explain Error plugin—or any AI-powered analysis—confirm that it aligns with your organization's guidelines.

## Instructions

### 1. Generate an API Key for OpenAI or Google AI

The Explain Error plugin requires access to an AI provider.

Choose one of the following providers and generate an API key:

- **OpenAI**

  - Go to: [https://platform.openai.com/](https://platform.openai.com/)
  - Sign in or create an account
  - Navigate to **API Keys**
  - Create a new API key and copy it somewhere secure

- **Google Gemini**

  - Go to: [https://ai.google.dev/](https://ai.google.dev/)
  - Sign in with a Google account
  - Create an API key from Google AI Studio
  - Copy the generated key

You'll use this key when configuring the plugin in Jenkins.

> [!NOTE]
> Additional providers may be supported in the future.

### 2. Install the Explain Error Plugin

1. In Jenkins, go to **Manage Jenkins**
2. Select **Manage Plugins**
3. Open the **Available** tab
4. Search for **Explain Error Plugin**
5. Select the plugin and choose **Install**

#### Plugin Configuration

Once the plugin is installed, it must be enabled and configured.

1. Go to **Manage Jenkins**
2. Select **Configure System**
3. Scroll down to the **Explain Error Plugin Configuration** section

Configure the following settings:

| Setting                     | Description                    | Recommended Value |
| --------------------------- | ------------------------------ | ----------------- |
| Enable AI Error Explanation | Turns the plugin on            | Enabled           |
| AI Provider                 | Select OpenAI or Google Gemini | Your choice       |
| API Key                     | Your provider’s API key        | Paste your key    |
| API URL                     | Custom endpoint (optional)     | Leave blank       |
| AI Model                    | Model name from your provider  | Required          |

After entering the configuration values:

1. Select **Test Configuration**
2. Confirm you see the message:
   **"Configuration test successful! API connection is working properly."**
3. Select **Save**

### 3. Create the Pipeline Job

Use the exercise files to create a pipeline job that intentionally fails in a way that produces a confusing stack trace.

1. Create a new **Pipeline** job named:
   **`use-ai-for-error-analysis`**

2. Use the pipeline configuration provided in the exercise files:

   - [`Jenkinsfile`](./Jenkinsfile)

3. Save the job configuration

4. Run the pipeline

5. Once the build fails, open the **Console Output** and review the errors

### 4. Use the Explain Error Plugin

Use the AI-enabled plugin to analyze the failure.

1. From the failed build, open the **Console Output**
2. Scroll to the top of the page
3. Select the **Explain Error** button

The plugin sends the console output to the configured AI provider and analyzes the failure.

After a short delay, the analysis results appear directly in the console output, including:

- **A summary of what caused the error**
- **Specific steps to resolve the issue**
- **Best practices to prevent similar problems**

Review each section and compare the AI explanation to what you initially inferred from the output.

## Next Steps

Reflect on how AI can help accelerate error resolution—especially when:

- You're working with unfamiliar codebases
- Errors originate from framework or metaprogramming behavior
- Stack traces are long, indirect, or misleading

Consider how tools like this might fit into your own CI/CD workflows.

## Shenanigans

### 1. Automatic AI Analysis

The Explain Error plugin includes a build step that can be used to generate an exaplanation.

Take a look at the `post` section in the following pipeline configuration:

- [auto-analysis.Jenkinsfile](./auto-analysis.Jenkinsfile)

```groovy
  post {
      failure {
          echo 'Build failed — generating AI explanation...'

          // Automatically analyze the failure using the Explain Error plugin
          explainError()

          echo 'AI analysis complete. Review the explanation in the console output.'
      }
  }
```

When you trigger the Explain Error plugin manually, Jenkins analyzes the console output *after* the build finishes and then waits for the response before displaying it.

By calling `explainError()` directly in the pipeline, the plugin captures and stashes the error analysis as part of the build’s execution.

That analysis is then made immediately available in the console output when the build completes.

In practice, this means you spend less time waiting on an explanation and more time understanding what went wrong—especially useful when you’re iterating on failing pipelines or reviewing errors from automated builds.

### 2. Why does the code fail?

For this demo, the Python project is intentionally designed to fail in a non-obvious way.

The code uses **metaclass programming** to automatically modify method behavior at runtime.

Review the following files:

- [`data_processor.py`](./data_processor.py)
- [`test_data_processor.py`](./test_data_processor.py)
- [`main.py`](./main.py)

The metaclass automatically wraps any method whose name starts with `get_`.

Each wrapped method is expected to return data in the following format:

```text
[
  {
    "data": {
      "value": <something>
    }
  }
]
```

The wrapper immediately attempts to extract the nested `value`.

When a method returns any of the following:

- An empty list
- A dictionary without the expected keys
- A differently structured result

...the failure occurs **inside the wrapper**, not inside the original method.

This leads to stack traces that appear disconnected from the code being tested—making the error difficult to diagnose without help.

Tools that use AI excel in scenarios like this by summarizing the root cause and highlighting exactly what the code returned.

<!-- FooterStart -->
[← 04_03 Use Test Results to Stop a Pipeline](../04_03_use_test_results/README.md) | [04_05 Challenge: Create artifacts and Reports →](../04_05_challenge_create_artifacts_reports/README.md)
<!-- FooterEnd -->
