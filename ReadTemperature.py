import sys
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
from datetime import datetime
import socket


dhtDevice = adafruit_dht.DHT11(board.D23)
deviceName = socket.gethostname()
# Getting the first command line argument as the directory path
directory_path = sys.argv[1] if len(sys.argv) > 1 else ""
tempValueFileFullPathName = directory_path + deviceName + "TempValue"
# Ensure there is a trailing slash in the directory path
if directory_path and not directory_path.endswith("/"):
    directory_path += "/"

while True:
    try:
        temperature_c = dhtDevice.temperature
        if temperature_c is not None:
            # Writing the temperature value to a file
            with open(tempValueFileFullPathName, "w") as file:
                file.write(f"{temperature_c}\n")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)
