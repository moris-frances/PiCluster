#!/bin/bash

DESTINATION="/home/morisfrances/BachelorProject/Software"
kill $(cat $DESTINATION/pid)
kill $(pgrep libgpiod_pulsei)
rm $DESTINATION/tempValue.txt