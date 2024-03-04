#!bin/sh

sudo apt-get update -y
sudo apt-get install build-essential python-dev -y
sudo apt install gpiod -y 
sudo apt install python3-pip -y
sudo pip3 install adafruit-circuitpython-dht -y
sudo apt install mpich -y
sudo apt-get install libopenmpi-dev -y
sudo apt-get install jq -y
sudo pip3 install mpi4py -y


cd /home/morisfrances/
mkdir BachelorProject
cd BachelorProject
mkdir Software