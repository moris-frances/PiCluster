#!/bin/bash

DESTINATION=$(cat config.json | jq -r ".destinationFolder")
kill $(cat $DESTINATION/pid)
kill $(pgrep libgpiod_pulsei)
rm $DESTINATION/tempValue.txt