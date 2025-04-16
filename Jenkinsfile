pipeline {
    agent {
        label 'docker-agent-python2'
    }
    stages {
        stage('Hello') {
            steps {
                echo "✅ Agent is working! Running on: ${env.NODE_NAME}"
                sh 'python3 --version'
            }
        }
    }
}
