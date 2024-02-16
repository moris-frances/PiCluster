#!/bin/bash

DESTINATION="/BachelorProject/Software/"
nohup python3 $DESTINATIONDHT11.py > $DESTINATIONlog.txt 2>&1 & echo $! > $DESTINATIONpid