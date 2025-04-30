import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec_to_bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range (0, 256):
        GPIO.output(dac, dec_to_bin(value))
        time.sleep(0.005)

        comp_val = GPIO.input(comp)

        if comp_val == 1:
            return value
    
    return 256

try:
    while True:
        enum_val = adc()
        voltage = (enum_val / 256) * 3.3
        print("enum_val = ", enum_val, "    |   voltage = {:.2f} V".format(voltage))
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()

