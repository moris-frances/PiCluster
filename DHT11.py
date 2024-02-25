import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
from datetime import date

dhtDevice = adafruit_dht.DHT11(board.D23)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Date: {s} Temp: {:.1f} F / {:.1f} C Luftfeuchtigkeit: {}%".format(date.today(), temperature_f, temperature_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)