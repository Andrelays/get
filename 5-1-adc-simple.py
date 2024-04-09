import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac,    GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp,   GPIO.IN)

def num_to_bin(num):
    str = bin(num)[2:].zfill(8)
    list = [int(digit) for digit in str]
    return list

def adc():
    for i in range(256):
        dac_value_list = num_to_bin(i)
        time.sleep(0.005)
        GPIO.output(dac, dac_value_list)
        time.sleep(0.005)
        comp_value = GPIO.input(comp)

        if (comp_value > 0):
            return i
    return 0

try:
    while (True):
        time_func = time.time()
        comp_value = adc()
        time_func = time.time() - time_func
        volt = comp_value / 256 * 3.3
        print(volt, "time =", time_func)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()