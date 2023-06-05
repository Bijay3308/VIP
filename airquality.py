import time
import Adafruit_ADS1x15  #pip install adafruit-circuitpython-ads1x15

# Create an ADS1x15 ADC instance
adc = Adafruit_ADS1x15.ADS1115()

# Specify the ADC channel (0-3)
channel = 0

# Read sensor data
air_quality_value = adc.read_adc(channel)

# Print sensor value
print(f'Air Quality: {air_quality_value}')
