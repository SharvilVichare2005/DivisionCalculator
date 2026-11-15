pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                if not exist .venv (
                    py -m venv .venv
                )
                .venv\\Scripts\\python -m pip install --upgrade pip
                .venv\\Scripts\\python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                .venv\\Scripts\\python -m pytest -v --junitxml=test-results.xml
                '''
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '''
                .venv\\Scripts\\python evidently_monitor.py
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'test-results.xml'

            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Division Calculator Pipeline Successful!'
        }

        failure {
            echo 'Division Calculator Pipeline Failed!'
        }
    }
}