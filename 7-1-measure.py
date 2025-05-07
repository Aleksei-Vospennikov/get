import RPi.GPIO as GPIO 
import time
import matplotlib.pyplot as plt

MAX_LIMIT = 0.8
MIN_LIMIT = 0.67
max_val = 255
sleep = 0.002

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
troyka = 13
comp = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def dec_to_bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    value = 128
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 64
    else:
        value += 64
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 32
    else:
        value += 32
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 16
    else:
        value += 16
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 8
    else:
        value += 8
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 4
    else:
        value += 4
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 2
    else:
        value += 2

    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 1
    else:
        value += 1
    
    GPIO.output(dac, dec_to_bin(value))
    time.sleep(sleep)
    if GPIO.input(comp) == 1:
        value -= 1

    return value

def output_leds(value):
    GPIO.output(leds, dec_to_bin(value))

def val_to_volt(value):
    return value / 255 * 3.3

data_voltage = []
data_time = []

GPIO.output(troyka, 0)

try:
    start_time = time.time()
    GPIO.output(troyka, 1)
    troyka_out = 0

    print("CHARGE ----------------------------------------------------------------------")

    while (troyka_out < max_val * MAX_LIMIT):
        troyka_out = adc()

        #print("troyka_out = ", troyka_out, "    |   voltage = {:.2f} V".format(val_to_volt(troyka_out)))

        data_voltage.append(troyka_out)
        data_time.append(time.time() - start_time)

        #time.sleep(0.005)

    print("DISCHARGE -------------------------------------------------------------------")

    GPIO.output(troyka, 0)
    troyka_out = adc()
    
    while (troyka_out > max_val * MIN_LIMIT):
        troyka_out = adc()

        #print("troyka_out = ", troyka_out, "    |   voltage = {:.2f} V".format(val_to_volt(troyka_out)))

        data_voltage.append(troyka_out)
        data_time.append(time.time() - start_time)

        #time.sleep(0.005)

    finish_time = time.time()
    duration = finish_time - start_time

    print("Experiment message:")
    print("duration     = ", duration)
    print("period       = ", duration / len(data_voltage))
    print("frequence    = ", len(data_voltage) / duration)
    print("quantization = ", (data_voltage[len(data_voltage) - 1] / len(data_voltage)))

    with open("data.txt", 'w') as data_file:
        for value in data_voltage:
            data_file.write("{:.2f}\n".format(value))

    with open("settings.txt", "w") as settings_file:
        settings_file.write("Average sampling rate = {:.2f}\n".format(len(data_voltage) / duration))
        settings_file.write("Quantization step = {:.2f}\n".format(data_voltage[len(data_voltage) - 1] / len(data_voltage)))

    plt.plot(data_time, data_voltage)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()




