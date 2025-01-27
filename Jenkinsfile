pipeline {
    agent any
    parameters {
        string(name: 'PROJECT_ID', default: 'helpful-passage-448119-d1')
        string(name: 'TOPIC_NAME', default: 'metrics-test')
        string(name: 'SERVICE_ACCOUNT_EMAIL', default: 'pubsub-publisher@helpful-passage-448119-d1.iam.gserviceaccount.com')
        string(name: 'MESSAGE', default: 'Hello from Jenkins!')
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
