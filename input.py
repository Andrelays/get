import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

GPIO.output(26, GPIO.input(24))
