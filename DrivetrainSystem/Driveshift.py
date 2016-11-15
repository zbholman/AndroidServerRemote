#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#Team: DriveTrain
#Author: Ghansyam Patel and Klaus Herchenroder
#Version: 6

from __future__ import division
import time
import sys

#Imports the PCA9685 Module.
import Adafruit_PCA9685

#Imports the PWM Adafruit Library
pwm = Adafruit_PCA9685.PCA9685()

#Configures Min and Max for the Servo Pulse Lengths
servo_min = 150
servo_max = 600
servo_neutral = 375
servo_drive = 400
steering_left = 300
steering_center = 355
steering_right = 420

#Helper Function to Make Setting a Servo Pulse Widht Simpler
def set_servo_pulse(channel, pulse):
  pulse_length = 1000000
  pulse_length //= 60
  print('{0}us per period'.format(pulse_length))
  pulse_length //= 4096
  print('{0}us per bit'.format(pulse_length))
  pulse *= 1000
  pulse //= pulse_length 
  pwm.set_pwm(channel, 0, pulse)
  
  

