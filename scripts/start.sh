#!/bin/bash
sudo mount rp1.local:/nfsDir /nfsDir
sudo exportfs -a
sudo systemctl start nfs-kernel-server.service
#Reading the destination(working directory) folder name from the "config.json" file
DESTINATION=$(cat ../config.json | jq -r ".destinationFolder")
#Reading the NFS directory(shared directory) folder name from the "config.json" file
NFS_DIR=$(cat ../config.json | jq -r ".nfs_dir")
#starting ReadTemperature.py in the background, saving output and errors to $DESTINATION/log.txt and its Process Identifier (PID) to $DESTINATION/pid
nohup python3 -u $DESTINATION/ReadTemperature.py $NFS_DIR > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid
