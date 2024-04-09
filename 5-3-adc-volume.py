import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac,    GPIO.OUT)
GPIO.setup(led,    GPIO.OUT)
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

def comp_to_disco(num):
    if (num == 0):
        return 8*[0]
    array = [int((i)*255/8) for i in range(8)]
    result = [1 if num >= array_elem else 0 for array_elem in array]

    return result

try:
    while (True):
        comp_value = adc()
        volt = comp_value / 256 * 3.3
        comp_list = comp_to_disco(comp_value)
        GPIO.output(led, comp_list)
        print(volt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()