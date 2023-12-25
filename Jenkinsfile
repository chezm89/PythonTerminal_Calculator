pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from your version control system
                checkout scm
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                // Create and activate virtual environment
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install project dependencies
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python unit tests
                script {
                    sh 'python test_calculator.py'
                }
            }
        }

        post {
        always {
            // Clean up: deactivate virtual environment
            script {
                sh 'deactivate'
            }
        }
    }


    }
}