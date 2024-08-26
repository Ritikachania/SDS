pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-django-app'  // Name of your Docker image
        DOCKER_TAG = 'latest'           // Tag for the Docker image
        K8S_DEPLOYMENT_FILE = 'k8s/deployment.yaml' // Path to your Kubernetes deployment file
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git url: 'https://github.com/Ritikachania/SDS.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create and activate the virtual environment, then install dependencies
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Django tests inside the virtual environment
                    sh '. venv/bin/activate && python3 manage.py test'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image and tag it
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes deployment file
                    sh 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
                }
            }
        }
    }

    post {
        always {
            // Actions to perform after every build, regardless of the result
            echo 'Pipeline completed.'
        }
        success {
            // Actions to perform only if the build was successful
            echo 'Build was successful!'
        }
        failure {
            // Actions to perform only if the build failed
            echo 'Build failed!'
        }
    }
}
