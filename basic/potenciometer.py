import machine
import utime

potenciometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    voltage = potenciometer.read_u16() * conversion_factor
    print(voltage)
    utime.sleep(2)