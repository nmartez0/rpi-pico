from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
# import framebuf

WIDTH = 128   # Oled display widht
HEIGHT = 32   # Oled display height

sda_pin = Pin(0)
scl_pin = Pin(1)

#I2C Initialisation 
i2c = I2C(0, scl=scl_pin, sda=sda_pin,freq=400000, timeout=50000)

# And a short delay to wait until the I2C port has finished activating.
utime.sleep_ms(200)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

device = i2c.scan()[0]

try:
    oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)                  # Init oled display
    oled.text("hello world", 5, 15)
    oled.show()
except Exception as err:
    print(f"Unable to initialize oled: {err}")

