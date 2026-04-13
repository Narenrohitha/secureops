pipeline {
    agent any

    environment {
        AWS_REGION      = 'us-east-1'
        ECR_REPO        = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/secureops-app"
        IMAGE_TAG       = "${BUILD_NUMBER}"
        SONAR_HOST      = "http://<SONARQUBE_IP>:9000"
        SONAR_PROJECT   = "secureops-app"
    }

    stages {

        stage('1 - Checkout Code') {
            steps {
                echo "=== Checking out source code ==="
                checkout scm
            }
        }

        stage('2 - SonarQube Analysis') {
            steps {
                echo "=== Running SonarQube code quality scan ==="
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=${SONAR_PROJECT} \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=${SONAR_HOST}
                    '''
                }
            }
        }

        stage('3 - Quality Gate') {
            steps {
                echo "=== Waiting for SonarQube Quality Gate ==="
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('4 - Trivy Filesystem Scan') {
            steps {
                echo "=== Scanning source code with Trivy ==="
                sh '''
                    trivy fs --exit-code 0 \
                      --severity HIGH,CRITICAL \
                      --format table \
                      -o trivy-fs-report.txt .
                    echo "--- Trivy FS Report ---"
                    cat trivy-fs-report.txt
                '''
                archiveArtifacts artifacts: 'trivy-fs-report.txt'
            }
        }

        stage('5 - Docker Build') {
            steps {
                echo "=== Building Docker image ==="
                sh '''
                    cd app
                    docker build -t ${ECR_REPO}:${IMAGE_TAG} .
                    docker tag  ${ECR_REPO}:${IMAGE_TAG} ${ECR_REPO}:latest
                    echo "Image built: ${ECR_REPO}:${IMAGE_TAG}"
                '''
            }
        }

        stage('6 - Trivy Image Scan') {
            steps {
                echo "=== Scanning Docker image with Trivy ==="
                sh '''
                    trivy image --exit-code 0 \
                      --severity HIGH,CRITICAL \
                      --format table \
                      -o trivy-image-report.txt \
                      ${ECR_REPO}:${IMAGE_TAG}
                    echo "--- Trivy Image Report ---"
                    cat trivy-image-report.txt
                '''
                archiveArtifacts artifacts: 'trivy-image-report.txt'
            }
        }

        stage('7 - Push to AWS ECR') {
            steps {
                echo "=== Pushing image to Amazon ECR ==="
                withAWS(credentials: 'aws-credentials', region: "${AWS_REGION}") {
                    sh '''
                        aws ecr get-login-password --region ${AWS_REGION} | \
                          docker login --username AWS \
                          --password-stdin \
                          ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

                        docker push ${ECR_REPO}:${IMAGE_TAG}
                        docker push ${ECR_REPO}:latest
                        echo "Pushed: ${ECR_REPO}:${IMAGE_TAG}"
                    '''
                }
            }
        }

        stage('8 - Update K8s Manifest') {
            steps {
                echo "=== Updating Kubernetes manifest for ArgoCD ==="
                withCredentials([usernamePassword(
                    credentialsId: 'github-credentials',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {
                    sh '''
                        git config user.email "jenkins@secureops.io"
                        git config user.name  "Jenkins CI"
                        sed -i "s|image: .*secureops-app:.*|image: ${ECR_REPO}:${IMAGE_TAG}|g" \
                          k8s/deployment.yaml
                        git add k8s/deployment.yaml
                        git commit -m "ci: bump image to build-${IMAGE_TAG} [skip ci]"
                        git push \
                          https://${GIT_USER}:${GIT_PASS}@github.com/YOUR_ORG/secureops.git \
                          HEAD:main
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "=== Cleaning workspace ==="
            cleanWs()
        }
        success {
            echo "BUILD ${BUILD_NUMBER} SUCCEEDED"
            slackSend color: 'good',
              message: "✅ *SecureOps Build ${BUILD_NUMBER} PASSED*\nImage: `${ECR_REPO}:${IMAGE_TAG}`\nJob: ${BUILD_URL}"
        }
        failure {
            echo "BUILD ${BUILD_NUMBER} FAILED"
            slackSend color: 'danger',
              message: "❌ *SecureOps Build ${BUILD_NUMBER} FAILED*\nCheck: ${BUILD_URL}"
        }
    }
}
