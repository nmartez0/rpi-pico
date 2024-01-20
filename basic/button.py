import machine
import utime

led_external = machine.Pin(0, machine.Pin.OUT)
buzzer = machine.Pin(8, machine.Pin.OUT)
button_k1 = machine.Pin(15,machine.Pin.IN)


# print("Hello")

while True:
    if button_k1.value() == 0:
        led_external.value(1)
        # buzzer.value(1)
        utime.sleep(2)
    else:
        led_external.value(0)
        # buzzer.value(0)
