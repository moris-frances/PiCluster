import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
from datetime import datetime

dhtDevice = adafruit_dht.DHT11(board.D23)

while True:
    try:
        temperature_c = dhtDevice.temperature
        if temperature_c is not None:
            # Writing the temperature value to a file
            with open("tempValue.txt", "w") as file:
                file.write(f"{temperature_c}\n")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)