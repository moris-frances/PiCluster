#!/bin/bash

DESTINATION=$(cat ../config.json | jq -r ".destinationFolder")
NFS_DIR=$(cat ../config.json | jq -r ".nfs_dir")

# nohup python3 -u $DESTINATION/ReadTemperature.py > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid
nohup python3 -u $DESTINATION/ReadTemperature.py $NFS_DIR > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid