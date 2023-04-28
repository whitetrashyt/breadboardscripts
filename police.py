import time
import RPi.GPIO as gpio #rpi gpio library

led_blue = 16
led_red = 15
ac_buzz= 18
#setup settings
gpio.setmode(gpio.BOARD)
gpio.setup(led_blue,gpio.OUT)
gpio.setup(led_red,gpio.OUT)
gpio.setup(ac_buzz,gpio.OUT)


#loop function
def loop(x):
    #while loooop
    while True:
        time.sleep(x)
        #print for debug
        print("blue + siren high!!")
        gpio.output(led_blue,gpio.HIGH)
        gpio.output(led_red,gpio.LOW)
        gpio.output(ac_buzz,gpio.HIGH)
        time.sleep(x)
        print("red + siren low!!")
        gpio.output(led_blue,gpio.LOW)
        gpio.output(led_red,gpio.HIGH)
        gpio.output(ac_buzz,gpio.LOW)
#to make sure everything is good before we run
gpio.cleanup

loop(1)