How to run the project:

    This guide assumes that the user is using Raspberry Pi devices that run Raspberry Pi OS (see ProjectDocumentation.pdf 2.3.1.1), are connected to the same local network thougether with a personal computer (see ProjectDocumentation.pdf 2.3.1.2), are configured to create "SSH" to one another without requiring password authentication (see ProjectDocumentation.pdf 2.3.1.3), have the "DHT11" sensors properly wired (see ProjectDocumentation.pdf 2.3.2.1) and has an updated mpiHostFile (see ProjectDocumentation.pdf 2.3.3.1)

1. Copy the folder with all of its contents to an identical directory on all of the nodes (Raspberry Pi devices) 

2. Write the path of said directory to the "destinationFolder" property of the "config.json" configuration file and the hostnames of all of the nodes (Raspberry Pi devices) to the "nodes" property
3. Run the ./scripts/setup.sh script on all devices. This will install needed dependacies and make directories that the project needs to use

4. On the main node (the node that the mpiexec script will be run on), in the 
/etc/exports file, append "/nfsDir *(rw,sync,no_subtree_check)", save and run the following commands in succession: "sudo exportfs -a", "sudo systemctl start nfs-kernel-server.service" in order to make the "/nfsDir" accessible to other nodes

5. On all nodes, run "sudo mount <mainNodeHostName>.local:/nfsDir /nfsDir". This command mounts the /nfsDir directory from the main node on all other nodes
Example: sudo mount rp1.local:/nfsDir /nfsDir

6. Run the setup.sh script on all devices from the "scripts" folder (if ran in another folder, the configuration file will not be found). This will start the "ReadTemperature.py" script in the background

7. On the main node, in the root of the working directory, run "mpiexec -n <NumberOfNodes> -hostfile mpiHostfile python3 BenchMarkScriptWithTemperature.py"
Example: mpiexec -n 3 -hostfile mpiHostfile python3 BenchMarkScriptWithTemperature.py
