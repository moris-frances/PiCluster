#!/bin/bash

DESTINATION="/home/morisfrances/BachelorProject/Software"
kill $(cat $DESTINATION/pid)
rm $DESTINATION/log.txt