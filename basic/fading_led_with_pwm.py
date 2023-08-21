import machine
import utime

led = machine.PWM(machine.Pin(10))
led.freq(1000)
temp_sensor = machine.ADC(4)
potenciometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    # voltage = potenciometer.read_u16() * conversion_factor
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    led.duty_u16(int(temperature * 1000))
    print(int(temperature * 1000))
    utime.sleep(1)