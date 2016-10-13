#IST 440
#10/13/2016
#Author: Ghansyam Patel
#Drive the Car Forward and Reverse 

import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

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
# tf =pio.output(11, False)
     Time Frame
def turn_right(tf):
    init()
    gpio.output(7, False)
    ggpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
    
def key_input(event):
    init()
    print('DriveMode:', event.char)
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'd':
        forward(sleep_time)
    elif key_press.lower() == 'r':
        reverse(sleep_time)
    elif key_press.lower() == 'l':
        turn_left(sleep_time)
    elif key_press.lower() == 't':
        turn_right(sleep_time)
    else:
        pass

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
    
        
