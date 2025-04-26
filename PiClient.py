import requests
import os
import time
import sys  
import time  
import board 
import adafruit_dht  
import RPi.GPIO as GPIO 
from datetime import datetime
import socket

# Initialize the DHT11 sensor; D23 refers to the GPIO pin the sensor is connected to
dhtDevice = adafruit_dht.DHT11(board.D23)
# Server URK
url = "localhost:8084/uploadValue"
# Get the hostname of the device for file naming
deviceName = socket.gethostname()

def sendRequest(endpoint, device, value):
    # Parameters for the POST request
    params = {
        # 'device': device_name,
        'device': device,
        'value': value
    }

    try:
        # Send a POST request and set a timeout
        response = requests.post(endpoint, params=params, timeout=10)  # 10 seconds timeout

        # Check if the response was successful
        if response.status_code == 200:
            print("Success:", response.text)
        else:
            print("Error:", response.status_code, response.text)

    except requests.exceptions.Timeout:
        # Handle cases for a timeout
        print("Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        # Handle other possible exceptions
        print("An error occurred:", str(e))

# Continuously read and write sensor data to a file
while True:
    try:
        # Read temperature in Celsius from the sensor
        temperature_c = dhtDevice.temperature
        if temperature_c is not None:
            sendRequest(url, deviceName, temperature_c)
    except RuntimeError as error:  # Handle runtime errors from the sensor
        print(error.args[0])
        time.sleep(2.0) 
        continue   
    except Exception as error: 
        dhtDevice.exit()  
        raise error 
    time.sleep(1)                # Wait for 1 second before the next read
