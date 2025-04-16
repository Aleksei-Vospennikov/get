import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec_to_bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

val = 0
flag = 1

try:
    period = float(input("Enter a period: "))
    while True:
        GPIO.output(dac, dec_to_bin(val))

        if val == 0:
            flag = 1
        elif val == 255:
            flag = 0

        if flag == 1:
            val += 1
        else:
            val -= 1

        time.sleep(period/510)
except Exception:
    print("Entered value is not a number. Try again.\n")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()