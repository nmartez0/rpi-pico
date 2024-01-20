import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
red_led = machine.Pin(15, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_alarm_handler(pin):
    print("ALARM! Motion detected!")
    green_led.value(0)
    for _ in range(50):
        red_led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)

def pir_normal_handler(pin):
    print("Everything is fine")
    red_led.value(0)
    while True:
        green_led.toggle()
        utime.sleep(2) 

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_alarm_handler)
sensor_pir.irq(trigger=machine.Pin.IRQ_FALLING, handler=pir_normal_handler)

while True:
    green_led.toggle()
    utime.sleep(2) 