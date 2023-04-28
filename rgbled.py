
#libraries
import RPi.GPIO as GPIO
from time import sleep
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BOARD)
#set red,green and blue pins
redpin = 11
greenpin = 13
bluepin = 15
#set pins as outputs
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)
def blink(pin):
      GPIO.output(pin, GPIO.HIGH)
      sleep(5)
      GPIO.output(pin, GPIO.LOW)
def turnOff():
    print('off')
    GPIO.output(redpin,0)
    GPIO.output(greenpin,0)
    GPIO.output(bluepin,0)
    
def white():
    print('white')
    blink(redpin)
    blink(greenpin)
    blink(bluepin)
    
def red():
    print('red')
    blink(redpin)
def green():
    print('green')
    blink(greenpin)
def blue():
    print('blue')
    blink(bluepin)
    
def yellow():
    print('yellow')
    blink(redpin)
    blink(greenpin)
    
def purple():
    print('ourple')
    blink(redpin)
    blink(bluepin)    
def lightBlue():
    print('light blue')
    blink(greenpin)
    blink(bluepin)
while True:
    sleep(5) #1second
    white()
    sleep(5)
    red()
    sleep(5)
    green()
    sleep(5)
    blue()
    sleep(5)
    yellow()
    sleep(5)
    purple()
    sleep(5)
    lightBlue()
    sleep(5)