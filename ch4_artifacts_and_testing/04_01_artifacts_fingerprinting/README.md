# 04_01 Artifacts and Fingerprinting

## **What is an Artifact?**

- An artifact is any file a Jenkins job creates that needs to be saved after a build.
- Examples include compiled binaries (ZIP files, Docker images) and text-based outputs (reports, logs, documents).

## **Archiving Artifacts**

- Jenkins provides the `archiveArtifacts` step to save files produced during a build.
- This step is commonly placed in the `post` section of a pipeline.
- The `post` block runs after all pipeline stages complete, ensuring artifacts are archived regardless of build logic.

## **Sharing Artifacts Between Jobs**

- To use artifacts created by another job, Jenkins relies on the **Copy Artifact plugin**.
- This plugin allows one job to pull artifacts from a different job.

## **Artifact Security**

- Artifact sharing is restricted by default.
- The job that creates the artifact must explicitly grant permission for other jobs to copy it.

## **Tracking Artifact Usage with Fingerprinting**

- Jenkins can track where artifacts are created and used through **fingerprinting**.
- When an artifact is created or accessed, Jenkins generates an MD5 checksum for the file.
- This checksum becomes the artifact’s fingerprint and is stored in Jenkins’ internal database.
- Fingerprints allow Jenkins to identify which jobs produced an artifact and which jobs later consumed it.

## Artifact Management with the Copy Artifact Plugin

In this lab, you will create and share build artifacts between Jenkins pipeline jobs. You will first generate and archive an artifact, then copy and analyze that artifact from a second pipeline.

This lab demonstrates artifact archiving, cross-job artifact access, permissions, and fingerprinting.

## **Overview**

You will complete the following steps in this lab:

1. **Install the Copy Artifact Plugin** on your Jenkins server.
1. **Create a pipeline that generates and archives an artifact**.
1. **Configure artifact permissions** to allow access from another job.
1. **Create a second pipeline that copies the artifact** from the first job.
1. **Analyze and archive a derived artifact**.
1. **Review artifact fingerprints** to trace artifact usage.

This lab should take approximately **15 to 20 minutes** to complete.

## **Instructions**

### **1. Install the Copy Artifact Plugin**

1. From the Jenkins dashboard, select **Manage Jenkins**.
1. Select **Plugins**, then open the **Available plugins** tab.
1. Search for **Copy Artifact**.
1. Select the plugin and choose **Install** (restart Jenkins if prompted).
1. Confirm the plugin is installed before continuing.

### **2. Create the Artifact-Producing Pipeline**

1. From the Jenkins dashboard, select **New Item**.
1. Enter the name `create-artifact`.
1. Select **Pipeline**, then choose **OK**.
1. Scroll to the **Pipeline** section.
1. Set **Definition** to **Pipeline script**.
1. Paste the following pipeline configuration:

    ```groovy
    pipeline {
        agent any
        options {
            copyArtifactPermission 'read-artifact'
        }
        stages {
            stage('Create-Artifact') {
                steps {
                    sh "set > report.txt"
                }
            }
        }
        post {
            always {
                archiveArtifacts artifacts: 'report.txt',
                    allowEmptyArchive: true,
                    fingerprint: true,
                    followSymlinks: false,
                    onlyIfSuccessful: true
            }
        }
    }
    ```

1. Select **Save**.
1. Select **Build Now** to run the job.
1. Confirm that `report.txt` appears in the **Artifacts** section of the completed build.

### **3. Review Artifact Fingerprints**

1. Open a completed build of the `create-artifact` job.
1. Select **Artifacts**, then select `report.txt`.
1. Select **Fingerprint** to view tracking details.
1. Note that Jenkins records where the artifact was created and any future jobs that access it.

### **4. Create the Artifact-Consuming Pipeline**

1. From the Jenkins dashboard, select **New Item**.
1. Enter the name `read-artifact`.
1. Select **Pipeline**, then choose **OK**.
1. Scroll to the **Pipeline** section.
1. Paste the following pipeline configuration:

    ```groovy
    pipeline {
        agent any

        options {
            timestamps()
            buildDiscarder(logRotator(numToKeepStr: '20'))
        }

        environment {
            INCOMING_ARTIFACT = 'report.txt'
            ANALYSIS_ARTIFACT = 'url_extraction.txt'
        }

        stages {
            stage('Read-Artifact') {
                steps {
                    copyArtifacts projectName: 'create-artifact',
                        filter: env.INCOMING_ARTIFACT,
                        fingerprintArtifacts: true,
                        selector: lastSuccessful()
                }
            }

            stage('Analyze-Artifact') {
                steps {
                    sh '''
                    set -euo pipefail
                    mkdir -p analysis

                    {
                        echo "=== URL Extraction (from bash set output) ==="
                        echo "Captured at: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
                        echo

                        grep -E '_URL=' $INCOMING_ARTIFACT || true
                    } | sort > $ANALYSIS_ARTIFACT

                    echo "Preview:"
                    cat $ANALYSIS_ARTIFACT
                    '''

                    archiveArtifacts artifacts: env.ANALYSIS_ARTIFACT,
                        fingerprint: true
                }
            }
        }
    }
    ```

1. Select **Save**.

### **5. Run the Artifact-Reading Pipeline**

1. Ensure the `create-artifact` job has completed successfully.
1. Select **Build Now** for the `read-artifact` job.
1. Confirm that the pipeline copies `report.txt` from the previous job.
1. Verify that `url_extraction.txt` is created and archived.

### **6. Review Cross-Job Fingerprinting**

1. Open the archived `report.txt` fingerprint from the `create-artifact` job.
1. Observe that Jenkins lists both:

   - The job that created the artifact
   - The job that consumed the artifact

> [!TIP]
> Use the fingerprint view to trace artifact flow across pipelines.

## **Conclusion**

You have successfully shared artifacts between Jenkins pipelines using permissions and fingerprinting.

<!-- FooterStart -->
---
[← 03_05 Solution: Improve a Docker Agent Pipeline](../../ch3_agents_and_distributed_builds/03_05_solution_improve_a_docker_agent_pipeline/README.md) | [04_02 Publish Test Results and Code Coverage Reports →](../04_02_publish_reports/README.md)
<!-- FooterEnd -->
