# import required modules
from machine import ADC, Pin, I2C
import utime
 
# use variables instead of numbers:
soil = ADC(Pin(26)) # Soil moisture PIN reference
 
#Calibraton values
min_moisture=19200
max_moisture=49300
 
while True:

    # read moisture value and convert to percentage into the calibration range
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture)

    # print values
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")

    utime.sleep(1.0) # set a delay between readings    