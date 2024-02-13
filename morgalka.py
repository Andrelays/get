import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

for i in range(100):
    time.sleep(1)
    GPIO.output(26, 1)  
    time.sleep(1)
    GPIO.output(26, 0)
