pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-django-app'  // Name of your Docker image
        DOCKER_TAG = 'latest'           // Tag for the Docker image
        REGISTRY_CREDENTIALS = 'docker-hub-credentials' // Docker registry credentials ID
        GIT_CREDENTIALS = 'git-credentials-id' // Git credentials ID for Jenkins
        EC2_HOST = '51.20.143.31' // EC2 instance public DNS
        EC2_KEY_PATH = '/var/lib/jenkins/.ssh/id_rsa' // Path to your EC2 private key on Jenkins server
        EC2_DEPLOY_PATH = '/home/ec2-user/my-django-app' // Path on EC2 instance
    }
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git url: 'https://github.com/Ritikachania/SDS.git', branch: 'master', credentialsId: "${GIT_CREDENTIALS}"
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

        stage('Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub and push the image
                    withCredentials([usernamePassword(credentialsId: "${REGISTRY_CREDENTIALS}", usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh 'docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD'
                        sh 'docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} $DOCKER_HUB_USERNAME/${DOCKER_IMAGE}:${DOCKER_TAG}'
                        sh 'docker push $DOCKER_HUB_USERNAME/${DOCKER_IMAGE}:${DOCKER_TAG}'
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    // Deploy the Docker container to EC2
                    sh """
                        ssh -o StrictHostKeyChecking=no -i ${EC2_KEY_PATH} ec2-user@${EC2_HOST} "
                        cd ${EC2_DEPLOY_PATH} && \
                        docker-compose down && \
                        docker-compose pull && \
                        docker-compose up -d"
                    """
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
