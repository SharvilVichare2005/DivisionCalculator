pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Division Calculator project'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Program Files\\Python313\\python.exe" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=test-results.xml'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe evidently_monitor.py'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results.xml'
            archiveArtifacts artifacts: 'evidently_report.html', allowEmptyArchive: true
        }
    }
}