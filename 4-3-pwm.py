import RPi.GPIO as GPIO

pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 1000)

pwm.start(0)

try:
    while True:
        dc = input("Enter duty cycle coefficient in percent (or q to quit): ")
        try:
            dc = int(dc)
            if (dc > 100 or dc < 0):            
                print("Entered value is not a percentage. Try again.\n")
            else:                            
                pwm.ChangeDutyCycle(dc)
                print("Expected voltage: {:.2f} V\n".format(dc / 100 * 3.3))

        except Exception:
            if dc == 'q':
                print("You've entered an exit-character. Bye-bye!\n")
                break
            else:
                print("Entered value is not a number. Try again.\n")

finally:
    pwm.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()

