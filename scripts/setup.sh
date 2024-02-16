#!bin/sh

sudo apt-get update
sudo apt-get install build-essential python-dev
sudo apt install gpiod        
sudo apt install python3-pip
sudo pip3 install adafruit-circuitpython-dht

cd /home/morisfrances/
mkdir BachelorProject
cd BachelorProject
mkdir Software