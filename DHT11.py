# Import necessary libraries
import time                     # Time module for handling time-related tasks
import board                    # Board module for accessing physical pins on hardware
import adafruit_dht             # Adafruit DHT library for DHT sensor reading
import RPi.GPIO as GPIO         # GPIO library for Raspberry Pi for pin control
from datetime import date       # Date module for getting current date

# Initialize the DHT11 sensor; D23 refers to the GPIO pin the sensor is connected to
dhtDevice = adafruit_dht.DHT11(board.D23)

# Continuously read and print the sensor data
while True:
    try:
        # Read temperature in Celsius from the sensor
        temperature_c = dhtDevice.temperature
        # Convert the temperature to Fahrenheit
        temperature_f = temperature_c * (9 / 5) + 32
        # Read humidity from the sensor
        humidity = dhtDevice.humidity
        # Print the current date
        print(date.today())
        # Print the temperature in Fahrenheit and Celsius, and humidity
        print("Temp: {:.1f} F / {:.1f} C Luftfeuchtigkeit: {}%".format(temperature_f, temperature_c, humidity))
    except RuntimeError as error:  # Handle runtime errors from the sensor
        print(error.args[0])       # Print the error message
        time.sleep(2.0)            # Wait for 2 seconds before retrying
        continue                   # Continue the loop
    except Exception as error:     # Handle other exceptions
        dhtDevice.exit()           # Cleanly exit the sensor connection
        raise error                # Re-raise the exception to stop the script
    time.sleep(2.0)                # Wait for 2 seconds before the next read
