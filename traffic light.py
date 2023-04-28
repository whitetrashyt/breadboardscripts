import time
import RPi.GPIO as gpio #rpi gpio library
led_green = 29
led_yellow = 7
led_red = 36

#setup settings
gpio.setmode(gpio.BOARD)
gpio.setup(led_green,gpio.OUT)
gpio.setup(led_yellow,gpio.OUT)
gpio.setup(led_red,gpio.OUT)
#loop function
def loop(x,y):
    #while loooop
    while True:
        time.sleep(x)
        #print for debug
        print("GREEN!!!!")
        gpio.output(led_green,gpio.HIGH)
        gpio.output(led_yellow,gpio.LOW)
        gpio.output(led_red,gpio.LOW)
        time.sleep(x)
        print("YELLOW!!!!")
        gpio.output(led_green,gpio.LOW)
        gpio.output(led_yellow,gpio.HIGH)
        gpio.output(led_red,gpio.LOW)
        time.sleep(y)
        print("RED!!!!")
        gpio.output(led_green,gpio.LOW)
        gpio.output(led_yellow,gpio.LOW)
        gpio.output(led_red,gpio.HIGH)
#to make sure everything is good before we run
gpio.cleanup
# default 8,6
loop(5,5)