pipeline {
    agent any
    stages {


        stage('Deploy code to Raspberry Pis') {
            steps {
                echo 'Deploying...'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    def sourceFiles = '*.py'
                    def destination = '//home/morisfrances/BachelorProject/Software/'
                    def startScript = 'python3 ' +  destination + 'DHT11.py > '+ destination +'log.txt &'
                    for(String server : servers){
                        deploy(server, sourceFiles, destination);
                        executeScript(server, startScript);
                    }
                }

            }
        }

        //     stage('Setup Raspberry Pis') {
        //     steps {
        //         echo 'Deploying...'
        //         script{
        //             def servers = ['rp1','rp2', 'rp3']
        //             def sourceFiles = '*.py'
        //             def destination = '//home/morisfrances/BachelorProject/Software/'
        //             def startScript = 'python3 ' +  destination + 'DHT11.py > '+ destination +'log.txt'
        //             def scripts = ['sudo apt-get update',
        //                             'sudo apt-get install build-essential python-dev',
        //                             'sudo apt install gpiod',           
        //                             'sudo apt install python3-pip',
        //                             'sudo pip3 install adafruit-circuitpython-dht',
        //                             'mkdir ']
        //             for(String server : servers){
        //                 for(String script : scripts){
        //                     executeScript(server, script);
        //                 }
        //             }
        //         }

        //     }
        // }
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
                                cleanRemote: false, excludes: '', execCommand: script, execTimeout: 120000, flatten: false, 
                                makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                remoteDirectory: '', 
                                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')
                            ],
                    usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                    ]
            )
}