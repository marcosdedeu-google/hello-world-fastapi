pipeline {
    agent any
    environment {
        PROJECT_ID = 'helpful-passage-448119-d1'
        TOPIC_NAME = 'metrics-test'
        SERVICE_ACCOUNT_EMAIL = 'pubsub-publisher@helpful-passage-448119-d1.iam.gserviceaccount.com'
        MESSAGE = 'Hello from Jenkins!'
    }

    stages {
        stage('Publish to Pub/Sub') {
            steps {
                sh '''
                    gcloud pubsub topics publish projects/${PROJECT_ID}/topics/${TOPIC_NAME} --message="${MESSAGE}" \
                        --impersonate-service-account=${SERVICE_ACCOUNT_EMAIL}
                '''
            }
        }
    }
}
