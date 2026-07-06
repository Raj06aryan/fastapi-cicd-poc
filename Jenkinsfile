pipeline{
    agent any

    stages{

        stage('Install Dependencies'){
            steps{
                sh '''
                    rm -rf .venv
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt

                '''
            }
        }

        stage('Run Tests'){
            steps{
                sh '. .venv/bin/python -m pytest'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh 'docker build -t fastapi-cicd:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy'){
            when{
                branch 'main'
            }
            steps{
                sh '''
                docker compose down
                docker compose up -d --build
                '''
            }
        }

        stage('health check'){
            when{
                branch 'main'
            }
            steps{
                sh 'curl --fail --retry 10 --retry-connrefused http://localhost:8000/health'
            }
        }
    }
}