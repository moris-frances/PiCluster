#!/bin/bash
#Reading the destination(working directory) folder name from the "config.json" file
DESTINATION=$(cat ../config.json | jq -r ".destinationFolder")
#Forcefully stops the execution of the ReadTemperature.py script 
kill $(cat $DESTINATION/pid)