pipeline {
    agent any
    stages {

        stage('Deploy code to Raspberry Pis') {
            steps {
                echo 'Deploying...'
                def servers = ['rp1','rp2', 'rp3']
                def sourceFiles = './*.py'
                def destination = '/home/morisfrances/Desktop/BA/project/software/PiCluster'

                for(String server : servers){
                    deploy(server, sourceFiles, destination);
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

    def deploy(server, sourceFiles, destination){

                sshPublisher(
                    publishers: 
                        [sshPublisherDesc(configName: server, 
                            transfers: 
                                [sshTransfer(
                                    cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, 
                                    makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                    remoteDirectory: destination, 
                                    remoteDirectorySDF: false, removePrefix: '', sourceFiles: sourceFiles)
                                ],
                        usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                        ]
                )
    }
}