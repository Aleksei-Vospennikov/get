import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, )
p.start(0)

try:
    while True:
        duty_cycle = 
        
        
finally:
    p.stop()
    GPIO.cleanup()
