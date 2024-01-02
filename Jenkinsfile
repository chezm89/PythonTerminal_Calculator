pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clean workspace before cloning
                    deleteDir()

                    // Clone the GitHub repository
                    git branch: 'main', url: 'https://github.com/chezm89/PythonTerminal_Calculator.git'
                }
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                // Create and activate virtual environment
                    withEnv(['PATH+PYTHON=venv/bin']){
                    sh '''
                        #!/bin/bash
                        python3 -m venv venv
                        . venv/bin/activate
                    '''
                }
                
            }
        }
            
        stage('Check Dir') {
            steps {
                sh '''
                    pwd
                    cd tests
                    ls
                    pwd
                    cd ../src
                    ls
                    pwd
                    cd ..
                    ls
                    pwd
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python unit tests
                sh 'python3 -m unittest tests.test_calculator'
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
