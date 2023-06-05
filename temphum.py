import Adafruit_DHT  #this library is needed to be pre-installed in the python


# Set the sensor type (DHT11 or DHT22) and GPIO pin number
sensor = Adafruit_DHT.DHT22
pin = 4

# Read sensor data
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Check if data was successfully retrieved
if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature:.2f}°C')
    print(f'Humidity: {humidity:.2f}%')
else:
    print('Failed to retrieve sensor data')
