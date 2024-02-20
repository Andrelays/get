import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
num = [0,  0, 0, 0, 0, 0,  0, 1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num) 
time.sleep(15)
GPIO.output(dac, 0) 
GPIO.cleanup()