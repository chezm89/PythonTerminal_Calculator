pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {

                 script {
                    // Check if the directory already exists
                    def repoDir = 'PythonTerminal_Calculator'
                    def dirExists = fileExists(repoDir)

                    // Clone the repository only if the directory doesn't exist
                    if (!dirExists) {
                        git clone 'https://github.com/chezm89/PythonTerminal_Calculator.git'
                        git pull
                    }
                }
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                // Create and activate virtual environment
                script {
                    sh '''
                        #!/bin/bash
                        python3 -m venv venv
                        . venv/bin/activate
                    '''
                }
                
            }
        }
        
        stage('Change Dir') {
            steps {
                script {
                    sh 'cd /var/lib/jenkins/workspace/PythonTerminal_Calculator'
                }
            }
        }
        
        stage('Print Python Path') {
            steps {
                script {
                    sh 'pwd'
                    sh 'python3 -c "import sys; print(sys.path)"'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python unit tests
                script {
                    sh 'python3 -m unittest test_calculator.py'
                }
            }
        }

        stage('Deactive Environment') {
            steps {
            // Clean up: deactivate virtual environment
            script {
                sh 'deactivate'
            }
        }
    }


    }
}