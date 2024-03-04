#!/bin/bash

DESTINATION="/home/morisfrances/BachelorProject/Software"
NFS_DIR="/nfsDir/"
# nohup python3 -u $DESTINATION/ReadTemperature.py > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid
nohup python3 -u $DESTINATION/ReadTemperature.py $NFS_DIR > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid