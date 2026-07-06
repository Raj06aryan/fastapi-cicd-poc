pipeline{
    agent any

    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }

        stage('Install Dependencies'){
            steps{
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests'){
            steps{
                sh '. .venv/bin/python -m pytest'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh 'docker build -t fastapi-cicd:latest .'
            }
        }

        stage('Deploy'){
            steps{
                sh '''
                docker compose down
                docker compose up -d --build
                '''
            }
        }

        stage('health check'){
            steps{
                sh 'curl http://localhost:8000/health'
            }
        }
    }
}