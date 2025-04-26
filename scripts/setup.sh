#!/bin/bash

#Installation of needed libraries and python modules
sudo apt-get update -y
sudo apt-get install build-essential python-dev -y
sudo apt install gpiod -y 
sudo apt install python3-pip -y
sudo pip3 install adafruit-circuitpython-dht
sudo apt install mpich -y
sudo apt-get install libopenmpi-dev -y
sudo apt-get install jq -y
sudo pip3 install mpi4py 

#Creation of shared directory for NFS
sudo mkdir /nfsDir
sudo chown -R nobody:nogroup /nfsDir                        
sudo chmod 777 /nfsDir