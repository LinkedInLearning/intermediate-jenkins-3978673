pipeline {
    agent any
    options {
        buildDiscarder(logRotator(daysToKeepStr: '10', numToKeepStr: '10'))
        timeout(time: 12, unit: 'HOURS')
    }
    stages {
        stage("Hello!\nPlease read the logs.") {
            steps {
                echo "Hello! Thanks for visiting the GitHub repsoitory for the LinkedIn Learning course \"Intermediate Jenkins\".\n\nIf you are working with the exercise files and see this message, you have successfully connected to the repo.\n\nIf you are using the repo with a specific lesson, you will need to update your project configuration to use the path to the Jenkinsfile for that lesson.\n\nFor example, if you are working with lesson 04_02, you will need to update the 'Script Path' in the SCM configuration to use:\n\n\tch4_artifacts_and_testing/04_02_publish_test_results_code_coverage_reports/Jenkinsfile\n\nThanks again for checking out this repo!"
            }
        }
    }
}
