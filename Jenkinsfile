pipeline {
    agent any

    environment {
        IMAGE_NAME = "nandhiyan/aceest-fitness-gym"
        IMAGE_TAG = "v3.0.0"
        DOCKER_CREDENTIALS_ID = "nandhiya-docker-hub-cred"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                rm -rf .venv
                python3 -m venv .venv
                . .venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . .venv/bin/activate
                python -m pytest -v
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube-server') {
                sh '''
                . .venv/bin/activate
                sonar-scanner
                '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Run Tests Inside Docker Container') {
            steps {
                sh '''
                docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python -m pytest -v
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: "${DOCKER_CREDENTIALS_ID}", url: "https://index.docker.io/v1/"]) {
                    sh '''
                    docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${IMAGE_NAME}:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Build, test, Docker image creation and DockerHub push completed successfully."
        }
        failure {
            echo "Pipeline failed. Check Jenkins console logs."
        }
    }
}