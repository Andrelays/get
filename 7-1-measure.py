import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

GPIO.setmode(GPIO.BCM)

data = []
settings = []
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac,    GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
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
        comp_value = 0
        time_func = time.time()
        GPIO.output(troyka, 1)

        while(comp_value < 206):
            comp_value = adc()
            volt = comp_value / 256 * 3.3
            data.append(comp_value)
            print(comp_value, "volt = ", volt)
            
        GPIO.output(troyka, 0)

        while(comp_value > 193):
            comp_value = adc()
            volt = comp_value / 256 * 3.3
            data.append(comp_value)
            print(comp_value, "volt = ", volt)

        time_func = time.time() - time_func
        print("time =", time_func)

        plt.plot(data)
        plt.show()

        settings.append(time_func / len(data))
        settings.append(time_func / len(data) * 33 / 255)

        data_str = [str(item) for item in data]
        settings_str = [str(item) for item in settings]
        print(data, data_str)

        with open("data.txt", "w") as outfile:
            outfile.write("\n".join(data_str))

        with open("settings.txt", "w") as outfile:
            outfile.write("\n".join(settings_str))

        settings = []
        data = []
finally:
    # plt.plot([10, 22, 33, 66, 22,])
    # plt.show()
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()