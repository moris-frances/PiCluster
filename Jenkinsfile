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
        stage('Generate mpiHostfile and deploy') {
            steps {
                echo 'Deploying...'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    def mpiHostfile = 'mpiHostfile'
                    def destination = '//home/morisfrances/BachelorProject/Software/'
                    def mpiHostFileGenScript = 'echo '
                    //generate server mpiHostFile Generation script
                    for(String server : servers){
                        mpiHostFileGenScript = mpiHostFileGenScript + '''$(nmap ''' + server + '''.local -oG - | awk '/Up$/{print $2}' | sort -V)''' + "\\n"
                    }
                    echo(mpiHostFileGenScript)
                    mpiHostFileGenScript = mpiHostFileGenScript + ' > ' + mpiHostfile
                    sh(mpiHostFileGenScript)
                    for(String server : servers){
                        deploy(server, mpiHostfile, destination);
                    }
                }

            }
        }
        stage('Deploy code to Raspberry Pis') {
            steps {
                echo 'Deploying...'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    def pyFiles = '*.py'
                    def scriptFiles = 'scripts/*.sh'
                    def mpiHostfile = 'mpiHostfile'
                    def destination = '//home/morisfrances/BachelorProject/Software/'
                    for(String server : servers){
                        deploy(server, mpiHostfile, destination);
                        deploy(server, scriptFiles, destination);
                        deploy(server, pyFiles, destination);
                    }
                }

            }
        }
        stage('Reboot the Raspberry Pis') {
            steps {
                echo 'Rebooting Raspberry Pis'
                script{
                    def servers = ['rp1','rp2', 'rp3']
                    for(String server : servers){
                        executeScript(server, '(sleep 1 ; sudo reboot) &');
                    }
                    sleep(15)
                }

            }
        }
        // stage('Start newly deployed scripts on the Raspberry Pis') {
        //     steps {
        //         echo 'Stopping running instance and starting a new one'
        //         script{
        //             def servers = ['rp1','rp2', 'rp3']
        //             def destination = '//home/morisfrances/BachelorProject/Software/'
                    
        //             def stopScript = destination + 'scripts/stop.sh'
        //             def startScript = destination + 'scripts/start.sh'
        //             def chmodScript = 'chmod ugo+x ' + stopScript + ' ' + startScript
        //             for(String server : servers){
        //                 executeScript(server, chmodScript);
        //                 executeScript(server, stopScript);
        //                 executeScript(server, startScript);
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
                                cleanRemote: false, excludes: '', execCommand: script, execTimeout: 1000000, flatten: false, 
                                makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                remoteDirectory: '', 
                                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')
                            ],
                    usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                    ]
            )
}