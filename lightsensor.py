import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
pin = 17

# Set pin as input
GPIO.setup(pin, GPIO.IN)

# Read sensor data
light_value = GPIO.input(pin)

# Print sensor value
print(f'Light Value: {light_value}')
