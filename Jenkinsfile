pipeline {
    agent any
    stages {

        stage('Deploy code to Raspberry Pis') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    post{
        success{
            echo "Finished pipeline for commit ${env.GIT_COMMIT}"
        }
        failure{
            echo 'Unsuccesful Run'
        }
    }
}