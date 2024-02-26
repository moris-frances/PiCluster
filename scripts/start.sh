#!/bin/bash

DESTINATION="/home/morisfrances/BachelorProject/Software"
# nohup python3 -u $DESTINATION/ReadTemperature.py > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid
python3 -u $DESTINATION/ReadTemperature.py & echo $! > $DESTINATION/pid