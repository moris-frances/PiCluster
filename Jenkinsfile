pipeline {
    agent any
    stages {
        stage('Read Configuration') {
            steps {
                script {
                    // Read configuration from the JSON file
                    echo "Reading configuration..."
                    def config = readJSON file: 'config.json'
                    env.DESTINATION = config.destinationFolder
                    env.SERVERS = config.nodes.join(',')
                }
            }
        }
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
                    def servers = env.SERVERS.tokenize(',')
                    def mpiHostfile = 'mpiHostfile'
                    def destination = '/' + env.DESTINATION
                    def mpiHostFileGenScript = 'echo \"'
                    //generate server mpiHostFile Generation script
                    for(String server : servers){
                        mpiHostFileGenScript = mpiHostFileGenScript + '''$(nmap ''' + server + '''.local -oG - | awk '/Up$/{print $2}' | sort -V) ''' + '\\n'
                    }
                    echo(mpiHostFileGenScript)
                    mpiHostFileGenScript = mpiHostFileGenScript + '\" > ' + mpiHostfile
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
                    def servers = env.SERVERS.tokenize(',')
                    def pyFiles = '*.py'
                    def scriptFiles = 'scripts/*.sh'
                    def mpiHostfile = 'mpiHostfile'
                    def configFile = 'config.json'
                    def destination = '/' + env.DESTINATION
                    for(String server : servers){
                        deploy(server, mpiHostfile, destination);
                        deploy(server, scriptFiles, destination);
                        deploy(server, configFile, destination);
                        deploy(server, pyFiles, destination);
                    }
                }

            }
        }
        // stage('Reboot the Raspberry Pis') {
        //     steps {
        //         echo 'Rebooting Raspberry Pis'
        //         script{
        //             def servers = ['rp1','rp2', 'rp3']
        //             for(String server : servers){
        //                 executeScript(server, '(sleep 1 ; sudo reboot) &');
        //             }
        //             sleep(25)
        //         }

        //     }
        // }
        // stage('Start newly deployed scripts on the Raspberry Pis') {
        //     steps {
        //         echo 'Stopping running instance and starting a new one'
        //         script{
        //             def servers = ['rp1','rp2', 'rp3']
        //             def destination = '//home/morisfrances/BachelorProject/Software/'
                    
        //             def stopScript = destination + 'scripts/stop.sh'
        //             def startScript = destination + 'scripts/start.sh'
        //             def chmodScript = 'chmod ugo+x ' + stopScript + ' ' + startScript
        //             def mountScript = "sudo mount " + servers[0] + ".local:/nfsDir /nfsDir"
        //             executeScript(servers[0], "sudo systemctl restart nfs-kernel-server")
        //             for(String server : servers){
        //                 executeScript(server, mountScript)
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
                                cleanRemote: false, excludes: '', execCommand: script, execTimeout: 100000, flatten: false, 
                                makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[, ]+', 
                                remoteDirectory: '', 
                                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')
                            ],
                    usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)
                    ]
            )
}