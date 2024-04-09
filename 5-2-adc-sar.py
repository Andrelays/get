import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
time_func = 0
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
    num = 0
    for i in range(7, -1, -1):
        num += 2**i
        num_list = num_to_bin(num) 
        GPIO.output(dac, num_list)
        time.sleep(0.002)
        comp_value = GPIO.input(comp)
        if (comp_value >= 0.95 and comp_value <= 1.05):
            num -= 2**i
    return num

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