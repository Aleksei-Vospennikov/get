import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0] * len(dac)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


#number = [1] * len(dac)
#number = [0, 1, 1, 1, 1, 1, 1, 1]
#number = [0, 1, 0, 0, 0, 0, 0, 0]
#number = [0, 0, 1, 0, 0, 0, 0, 0]
#number = [0, 0, 0, 0, 0, 1, 0, 1]
number = [0] * len(dac)

GPIO.output(dac, number)
time.sleep(10)


GPIO.output(dac, 0)
GPIO.cleanup()
