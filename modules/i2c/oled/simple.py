import machine
import utime
from ssd1306 import SSD1306_I2C

WIDTH = 128   # Oled display widht
HEIGHT = 32   # Oled display height

# Display
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
device = i2c.scan()[0]

# Temp sensor
adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)

try:
    while True:
        reading = adc.read_u16() * conversion_factor
        temperature = 25 - (reading - 0.706)/0.001721
        oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)                  # Init oled display
        oled.text("Temp: " + str(temperature), 10, 15)
        oled.show()
        utime.sleep(2)
except Exception as err:
    print(f"Unable to initialize oled: {err}")