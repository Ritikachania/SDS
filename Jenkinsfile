pipeline {
    agent any

    environment {
        // Environment variables for Docker image and Kubernetes context
        DOCKER_IMAGE = 'my-django-app'
        DOCKER_TAG = 'latest'
        K8S_DEPLOYMENT_FILE = 'k8s/deployment.yaml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Ritikachania/SDS.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure the virtual environment is set up and dependencies are installed
                    sh 'python -m venv venv || true'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment before running tests
                    sh '. venv/bin/activate && python manage.py test'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes deployment configuration
                    sh 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            // Optionally, clean up resources or perform other actions
        }
        success {
            echo 'Build was successful!'
            // Optionally, send notifications or trigger other actions
        }
        failure {
            echo 'Build failed!'
            // Optionally, send failure notifications or perform other actions
        }
    }
}
