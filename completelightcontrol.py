import RPi.GPIO as GPIO
import time
# define your leds
# they don't need to be referred to as "led_1" etc. always but for cases like these where
# we may have more than one colored led we use a numerical nomenclature to avoid having names
# like led_red1, led_red2, so on so forth
led_1 = 33
led_2 = 31
led_3 = 29
# list for iterating
leds = [led_1,led_2,led_3]
GPIO.setmode(GPIO.BOARD)
# this is only a temporary setup
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.setup(led_3,GPIO.OUT)
# blink function
def blink(x,y):
    GPIO.output(x,1) # instead of typing GPIO.HIGH, we simply provide a boolean 1 or 0.
    time.sleep(y)
    GPIO.output(x,0)
# "leave-on" blink, to be used when led is on and we want to blink it off once.)
def onblink(v,w):
    GPIO.output(v,0)
    time.sleep(w)
    GPIO.output(w,1)
def duo_onblink(s,t,u): # double onblink
    GPIO.output(s,0)
    GPIO.output(t,0)
    time.sleep(u)
    GPIO.output(s,1)
    GPIO.output(t,1)
def tri_onblink(o,p,q,r):
    GPIO.output(o,0)
    GPIO.output(p,0)
    GPIO.output(q,0)
    time.sleep(r)
    GPIO.output(o,1)
    GPIO.output(p,1)
    GPIO.output(q,1)
# two light series function
def duoseries(a,b,c): # A is led 1, B is led 2, c is our delay.
    GPIO.output(a,1)
    time.sleep(c)
    GPIO.output(a,0)
    GPIO.output(b,1)
    time.sleep(c) # TO DO: seperate variable?
    GPIO.output(b,0)
# three light series function
def triseries(d,e,f,g): # where d, e, f are our leds and g is our delay
    GPIO.output(d,1)
    time.sleep(g)
    GPIO.output(d,0)
    GPIO.output(e,1)
    time.sleep(g)
    GPIO.output(e,0)
    GPIO.output(f,1)
    time.sleep(g)
    GPIO.output(f,0)
# two light sequence function
def duosequence(h,i,j): # where h, i are our leds and j is our delay.
    time.sleep(j) # for extra *pizaaz*
    GPIO.output(h,1)
    time.sleep(j)
    GPIO.output(i,1)
    time.sleep(j)
    while True:
        duo_onblink(h,i,0.1)
        time.sleep(0.5)
def trisequence(k,l,m,n):
    time.sleep(n) # for extra *pizaaz*
    GPIO.output(k,1)
    time.sleep(n)
    GPIO.output(l,1)
    time.sleep(n)
    GPIO.output(m,1)
    time.sleep(n)
    while True:
        tri_onblink(k,l,m,0.1)
        time.sleep(0.5)    
# Make sure all gpio output is nonexsistent
for i in leds:
    GPIO.output(i,0)
trisequence(led_1,led_2,led_3,1)