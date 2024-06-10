pipeline {
    agent any
    environment {
		TRANSLATE_BOT_TOKEN = credentials('translate_tg_bot_token')

		DOCKER_IMAGE = 'yatsyshynoleksandr/cursova_translate'
    }
    stages {
        stage('Start') {
            steps {
                echo 'Cursova_Bot'
            }
        }

        stage('Build Translate service') {
            steps {
                sh 'export TRANSLATE_BOT_TOKEN=$TRANSLATE_BOT_TOKEN'
                dir("Translate_botTg")
				{
					sh 'docker-compose build'
				}
				sh 'docker tag translate-tg_bot:latest $DOCKER_IMAGE:latest'
                sh 'docker tag translate-tg_bot:latest $DOCKER_IMAGE:$BUILD_NUMBER'

            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\n Branch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\n Failure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

		stage('Push to registry') {
            steps {
                withDockerRegistry([ credentialsId: "dockerhub_token", url: "" ])
                {
                    sh "docker push $DOCKER_IMAGE:latest"
                    sh "docker push $DOCKER_IMAGE:$BUILD_NUMBER"
                }
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

        stage('Deploy Translate service') {
            steps {
				dir("Translate_botTg"){
					sh "docker-compose down"
                	sh "docker container prune --force"
                	sh "docker image prune --force"
                	sh "docker-compose up -d --build"
				}
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }
    }

    post {
        success {
            script {
                // Send Telegram notification on success
                telegramSend message: "Job Name: ${env.JOB_NAME}\n Branch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}"
            }
        }
    }
}
