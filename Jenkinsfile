pipeline {
    agent any
    stages {
        // stage('Setup Raspberry Pis') {
        //         steps {
        //             echo 'Installing dependacies and setting project folders up'
        //             script{
        //                 def servers = ['rp1','rp2', 'rp3']
        //                 def script = './scripts/setup.sh'
        //                 for(String server : servers){
        //                     executeScript(server, script);
        //                 }
        //             }

        //         }
        // }
        stage('Deploy code to Raspberry Pis') {
            steps {
                echo 'Deploying...'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    def sourceFiles = '*.py'
                    def destination = '/BachelorProject/Software/'
                    for(String server : servers){
                        deploy(server, sourceFiles, destination);
                    }
                }

            }
        }
        stage('Start newly deployed scripts on the Raspberry Pis') {
            steps {
                echo 'Stopping running instance and starting a new one'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    def stopScript = './scripts/stop.sh'
                    def startScript = './scripts/start.sh'
                    for(String server : servers){
                        executeScript(server, stopScript);
                        executeScript(server, startScript);
                    }
                }

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
def deploy(server, sourceFiles, destination){

            sshPublisher(
                publishers: 
                    [sshPublisherDesc(configName: server, 
                        transfers: 
                            [sshTransfer(
                                cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, 
                                makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                remoteDirectory: destination, 
                                remoteDirectorySDF: false, removePrefix: '', sourceFiles: sourceFiles)
                            ],
                    usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                    ]
            )
}

def executeScript(server, script){

            sshPublisher(
                publishers: 
                    [sshPublisherDesc(configName: server, 
                        transfers: 
                            [sshTransfer(
                                cleanRemote: false, excludes: '', execCommand: script, execTimeout: 1000000, flatten: false, 
                                makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                remoteDirectory: '', 
                                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')
                            ],
                    usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                    ]
            )
}