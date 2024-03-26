import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        x = input("Write number 0 <= x <= 255\n")
        try:
            x = int(x)
            if 0 <= x <= 255:
                for i in range(8): GPIO.output(dac[i], dec2bin(x)[i])
                volt = float(x)/256*3.3
                print("Volt: ", volt)
            else:
                if (x < 0):   print("Negative number")
                if (x > 255): print("Number > 255")
        except Exception:
            if x == "q": break
            print("Not a number")            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")