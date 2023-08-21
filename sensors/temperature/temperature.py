import machine
import utime
from dht import DHT11

pin = machine.Pin(28, machine.Pin.OUT, machine.Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature()))
    print("Humidity: {}".format(sensor.humidity()))
    utime.sleep(2)