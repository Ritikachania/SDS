pipeline {
    agent any

    environment {
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
                    // Create and activate the virtual environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '. venv/bin/activate && python3 manage.py test'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build was successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
