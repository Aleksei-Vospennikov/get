import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec_to_bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        num = input("Enter a number from 0 to 255 (or q for exit): ")
        try:            
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec_to_bin(num))
                voltage = num / 256.0 * 3.3
                print("Output voltage: {:.4f} V\n".format(voltage))
            elif num < 0:
                print("Entered number is negative. Try again.\n")
            elif num > 255:
                print("Entered number exceeds the limit of 8-bit DAC. Try again.\n")
        except Exception:                                      
            if num == 'q':
                print("You've entered an exit-character. Bye-bye!\n")
                break
            else:
                try:
                    float(num) == num
                    print("Entered value is not an integer number. Try again.\n")
                except Exception:
                    print("Entered value is not a number. Try again.\n")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

