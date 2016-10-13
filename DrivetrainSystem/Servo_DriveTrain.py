#IST 440
#10/13/2016
#Author: Ghansyam Patel
#Drive the Car Forward and Reverse 

import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    
#FORWARD
# tf = Time Frame
def forward(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

#REVERSE
# tf = Time Frame
def reverse(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

#TURN LEFT
# tf = Time Frame
def turn_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

#TURN RIGHT
# tf = Time Frame
def turn_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
    
forward(2)
reverse(2)
turn_left(2)
turn_right(2)
