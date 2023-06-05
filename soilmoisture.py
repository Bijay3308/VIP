import time
import board
import adafruit_mcp3xxx.mcp3008 as MCP   #pip install adafruit-circuitpython-mcp3xxx

import adafruit_mcp3xxx.analog_in as AnalogIn

# Create an MCP3008 ADC instance
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

# Specify the ADC channel (0-7)
channel = AnalogIn(mcp, MCP.P0)

# Read sensor data
moisture_value = channel.value

# Print sensor value
print(f'Soil Moisture: {moisture_value}')
