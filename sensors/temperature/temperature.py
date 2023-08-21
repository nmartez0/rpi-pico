import machine
import utime
import dht

pin = machine.Pin(2)
sensor = dht.DHT11(pin)

while True:
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {}C".format(temp))
        print("Humidity: {}".format(humidity))
        utime.sleep(3)