# Basic documentation

## Electronic

### Diodes

Spanish
[Diodo LED](https://tallerelectronica.com/diodo-led/)
[Resistence Calculator](https://www.digikey.es/es/resources/conversion-calculators/conversion-calculator-resistor-color-code)

### Active buzzer

The TMB12A05 is an active buzzer that acts as an alarm or acustic signal when a voltage of 3V is supplied. With this buzzer you can mount projects that demands low voltage and where a simple but practical alarm is required.

Specifications:

- Operating voltage: 3.5 to 5 VDC.
- Operating power: <= 30mA.
- Sound Pressure Level (SPL): >= 85dB.
- Resonance frequency: 2300 ± 500Hz.
- Oscillator Circuit: Active (driven circuit included)
- Operating temperature: -20 a +60 degrees centigrades.
- Weight: 2 grams.
- Dimensions: 12×9.5mm

## MicroPython libraries

### Machine

Functions related to hardware

[Library](https://docs.micropython.org/en/latest/library/machine.html)

#### Classes

##### Pin

A pin object is used to control I/O pins (also known as GPIO - general-purpose input/output). Pin objects are commonly associated with a physical pin that can drive an output voltage and read input voltages. The pin class has methods to set the mode of the pin (IN, OUT, etc) and methods to get and set the digital logic level. For analog control of a pin, see the ADC class.

[Class Pin](https://docs.micropython.org/en/latest/library/machine.Pin.html)

##### Timer

Hardware timers deal with timing of periods and events. Timers are perhaps the most flexible and heterogeneous kind of hardware in MCUs and SoCs, differently greatly from a model to a model. MicroPython’s Timer class defines a baseline operation of executing a callback with a given period (or once after some delay), and allow specific boards to define more non-standard behaviour (which thus won’t be portable to other boards).

[Class Timer](https://docs.micropython.org/en/latest/library/machine.Timer.html)

##### PWM (pulse with modulation)

This class provides pulse width modulation output.

[Class PWM](https://docs.micropython.org/en/latest/library/machine.PWM.html)

### Time
