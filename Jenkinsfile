pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-django-app'  // Name of your Docker image
        DOCKER_TAG = 'latest'           // Tag for the Docker image
        REGISTRY_CREDENTIALS = 'docker-hub-credentials' // Credentials for Docker Hub
        GIT_CREDENTIALS = 'git-credentials-id' // Credentials for GitHub
        EC2_HOST = '13.51.108.130' // Your EC2 instance public IP
        EC2_KEY_PATH = '/var/lib/jenkins/.ssh/id_rsa' // Path to your EC2 private key on Jenkins server
        EC2_DEPLOY_PATH = '/home/ec2-user/SDS/SDS' // Path on EC2 instance
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git url: 'https://github.com/Ritikachania/SDS.git', branch: 'master'
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
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
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
                    // SSH into EC2 and deploy using Docker Compose
                    sh """
                        ssh -i ${EC2_KEY_PATH} ec2-user@${EC2_HOST} "mkdir -p ${EC2_DEPLOY_PATH} && cd ${EC2_DEPLOY_PATH} && docker-compose down && docker-compose pull && docker-compose up -d"
                    """
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
