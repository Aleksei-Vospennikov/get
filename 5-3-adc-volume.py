import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec_to_bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    value = 128
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 64
    else:
        value += 64
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 32
    else:
        value += 32
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 16
    else:
        value += 16
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 8
    else:
        value += 8
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 4
    else:
        value += 4
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 2
    else:
        value += 2

    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 1
    else:
        value += 1
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(0.005)
    if GPIO.input(comp) == 1:
        value -= 1

    return value

try:
    while True:
        enum_val = adc()        
        voltage = (enum_val / 256) * 3.3

        leds_val = 2 ** round((enum_val / 256) * 8) - 1
        GPIO.output(leds, dec_to_bin(leds_val))

        print("enum_val = ", enum_val, "    |   voltage = {:.2f} V".format(voltage))
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()