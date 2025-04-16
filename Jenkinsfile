pipeline {
    agent { 
        node {
            label 'docker-agent-python2'
            }
      }
    triggers{
	    pollSCM '*/1 * * * *' // check git repo every 1 minutes to see any changes, if changes made then run the jenkins
    }
    environment{
        DIRECTORY_PATH = 'https://github.com/tomadonna1/jenkins-cnn-test'
        TESTING_ENVIRONMENT = 'testing environment'
        PRODUCTION_ENVIRONMENT = 'production environment'
    }
    stages {
        stage('Build') {
            steps {
                echo "Fetch the source code from the directory path specified by the environment variable"
                echo "Fetching from: ${env.DIRECTORY_PATH}"
                sh 'pip install --break-system-packages -r requirements.txt'
                echo "Compile the code and generate any necessary artefacts"
            }
        }
        stage('Test') {
            steps {
                echo "Unit tests"
                echo "Integration tests"
            }
        }
        stage('Code Quality Check') {
            steps {
                echo "Check the quality of the code"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy the application to a testing environment specified by the environment variable"
                echo "Deploying to: ${env.TESTING_ENVIRONMENT}"
            }
        }
        stage('Approval') {
            steps {
                echo "Waiting for manual approval (simulated)..."
                sleep 10
            }
        }
        stage('Deploy to Production'){
            steps {
                echo "Deploying to the production environment: ${env.PRODUCTION_ENVIRONMENT}"
                echo "Running prediction test with client.py"
                sh '''
                python3 client.py
                '''
                post {
                    success{ echo "Post success "}
                    failure { echo "Post failed" }
                }
            }
        }
    }
}