import time
import RPi.GPIO as gpio #rpi gpio library


#setup settings
gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.OUT)

#loop function
def loop(x):
    #while loooop
    while True:
        time.sleep(x)
        #print for debug
        print("on!")
        gpio.output(16,gpio.HIGH)
        time.sleep(x)
        print("off!")
        gpio.output(16,gpio.LOW)
#to make sure everything is good before we run
gpio.cleanup

loop(0.3)