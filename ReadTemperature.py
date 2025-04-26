# Import necessary libraries
import sys                      # System-specific parameters and functions
import time                     # Time module for handling time-related tasks
import board                    # Board module for accessing physical pins on hardware
import adafruit_dht             # Adafruit DHT library for DHT sensor reading
import RPi.GPIO as GPIO         # GPIO library for Raspberry Pi for pin control
from datetime import datetime   # Datetime module for getting current date and time
import socket                   # Socket library for networking interface

# Initialize the DHT11 sensor; D23 refers to the GPIO pin the sensor is connected to
dhtDevice = adafruit_dht.DHT11(board.D23)

# Get the hostname of the device for file naming
deviceName = socket.gethostname()

# Check for command line argument for directory path; use it if provided
directory_path = sys.argv[1] if len(sys.argv) > 1 else ""
tempValueFileFullPathName = directory_path + deviceName + "TempValue"

# Ensure there is a trailing slash in the directory path
if directory_path and not directory_path.endswith("/"):
    directory_path += "/"

# Continuously read and write sensor data to a file
while True:
    try:
        # Read temperature in Celsius from the sensor
        temperature_c = dhtDevice.temperature
        if temperature_c is not None:
            # Write the temperature value to a file with a dynamic name
            with open(tempValueFileFullPathName, "w") as file:
                file.write(f"{temperature_c}\n")
    except RuntimeError as error:  # Handle runtime errors from the sensor
        print(error.args[0])       # Print the error message
        time.sleep(2.0)            # Wait for 2 seconds before retrying
        continue                   # Continue the loop
    except Exception as error:     # Handle other exceptions
        dhtDevice.exit()           # Cleanly exit the sensor connection
        raise error                # Re-raise the exception to stop the script
    time.sleep(2.0)                # Wait for 2 seconds before the next read
