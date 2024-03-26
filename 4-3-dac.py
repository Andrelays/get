import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 1000)

p.start(0)

try:
    while(1):
        x = int(input())
        p.ChangeDutyCycle(x)
        print("Volt: ", 3.3*x/100)

finally:
    p.stop()
    GPIO.output(27,0)
    GPIO.cleanup()