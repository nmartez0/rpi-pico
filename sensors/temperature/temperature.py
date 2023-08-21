import machine
import utime
from dht import DHT11

pin = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {}C".format(temp))
        print("Humidity: {}".format(humidity))
        utime.sleep(3)
        