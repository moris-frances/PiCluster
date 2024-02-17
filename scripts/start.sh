#!/bin/bash

DESTINATION="/BachelorProject/Software"
nohup python3 $DESTINATION/DHT11.py > $DESTINATION/log.txt 2>&1 & echo $! > $DESTINATION/pid