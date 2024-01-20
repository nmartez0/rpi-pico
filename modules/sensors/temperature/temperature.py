import machine
import utime
import dht
import ssd1306

# DHT11 Sensor
sensor_pin = machine.Pin(0)
sensor = dht.DHT11(sensor_pin)
result = sensor.measure()

# Display 128x32 
WIDTH = 128
HEIGH = 32
i2c = machine.I2C(0,sda=machine.Pin(4), scl=machine.Pin(5))
display = ssd1306.SSD1306_I2C(WIDTH,HEIGH,i2c)

while True:
    temperature  = (sensor.temperature())
    humidity = (sensor.humidity())
    display.text("Temp: {:.01f}C".format(temperature), 5,8)
    display.text("Hum:  {:.01f}%".format(humidity), 5, 16)
    display.show()
    utime.sleep(2)