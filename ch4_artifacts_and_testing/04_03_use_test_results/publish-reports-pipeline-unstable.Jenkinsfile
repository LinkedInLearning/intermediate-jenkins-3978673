pipeline {
    agent any

    environment {
        PROJECT_DIRECTORY = "ch4_artifacts_and_testing/04_03_use_test_results"
    }

    options {
        buildDiscarder(logRotator(daysToKeepStr: '10', numToKeepStr: '10'))
        timeout(time: 12, unit: 'HOURS')
        timestamps()
    }

    stages {
        stage('Requirements') {
            steps {
                // Check environment versions
                sh 'python3 --version'
                sh 'git --version'

                // Checkout code
                git branch: 'main',
                    url: 'https://github.com/LinkedInLearning/intermediate-jenkins-3978673.git'

                dir("${env.WORKSPACE}/${env.PROJECT_DIRECTORY}"){
                    // Create venv and install requirements
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip3 install --upgrade --requirement requirements.txt'
                }
            }
        }

        stage('Lint') {
            steps {
                dir("${env.WORKSPACE}/${env.PROJECT_DIRECTORY}"){
                    // Run flake8
                    sh 'venv/bin/flake8 --ignore=E501,E231 *.py'

                    // Run pylint, outputting results in JSON format
                    // Removed '--disable=C0326' which was reported as useless
                    sh 'venv/bin/pylint --errors-only --disable=C0301 --output-format=json *.py > pylint_report.json'
                }
            }
        }

        stage('Test') {
            steps {
                dir("${env.WORKSPACE}/${env.PROJECT_DIRECTORY}") {
                    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                        sh '''
                            venv/bin/coverage run -m pytest -v test_*.py \
                            --junitxml=pytest_junit.xml
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo "Build the application in this step..."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy the application in this step..."
            }
        }
    }

    post {
        always {
            dir("${env.WORKSPACE}/${env.PROJECT_DIRECTORY}") {

                // 1) Publish JUnit first so the UI gets test results whenever the XML exists
                junit(
                    testResults: 'pytest_junit.xml',
                    allowEmptyResults: true
                )

                // 2) Generate coverage.xml, but don't fail the post block if it can't be generated
                sh(
                    script: 'venv/bin/coverage xml || true',
                    label: 'Generate Cobertura XML'
                )

                // 3) Publish coverage if the file exists (recordCoverage will tolerate missing/parse issues)
                recordCoverage(
                    tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']],
                    enabledForFailure: true,
                    ignoreParsingErrors: true
                )

                // 4) Archive reports (also non-fatal)
                archiveArtifacts(
                    artifacts: '*.xml',
                    allowEmptyArchive: true,
                    fingerprint: true,
                    onlyIfSuccessful: false
                )
            }
        }
    }

}
