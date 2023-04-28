import time as t
import RPi.GPIO as gpio

pin_o = 15
pin_y = 24

#settings time
gpio.setmode(gpio.BOARD)
def discharge():
    gpio.setup(pin_y, gpio.IN)
    gpio.setup(pin_o, gpio.OUT)
    gpio.output(pin_o, False)
    t.sleep(0.004)

# this function provides a "charge timing"
def charge_time():
    gpio.setup(pin_y, gpio.OUT)
    gpio.setup(pin_o, gpio.IN)
    count = 0
    gpio.output(pin_y, True)
    while not gpio.input(pin_y):
        count = count + 1
    return count
# reads the output
def analog_read():
    discharge()
    return charge_time()

#finally read loop
while True:
    print(analog_read())
    t.sleep(1)