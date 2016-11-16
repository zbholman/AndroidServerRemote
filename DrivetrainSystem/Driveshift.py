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

#Set Frequency to 60Hz for the Servos
pwm.set_pwm_freq(60)

#To Quit 
print('Moving Servo on channel 0, Press Ctrl-C To Quit')

while True:
  print"Drive Mode:",
  mode = raw_input()
  
  if (mode == 'p'):
    print('Stop')
    pwm.set_pwm(0, 0, servo_neutral)
    
  elif (mode == 's'):
    pwm.set_pwm(1, 1, steering_center)
    if servo_drive > 375:
      servo_drive = servo_drive - (((servo_drive - 375) * 2) + 16)
    pwm.set_pwm(0, 0, servo_drive)
  
  elif (mode == 'w'):
    pwm.set_pwm(1, 1, steering_center)
    if servo_drive < 359:
      servo_drive = servo_drive + (((359 - servo_drive) *2) + 16)
    pwm.set_pwm(0, 0, servo_drive)
    
  elif (mode == 'n'):
    pwm.set_pwm(0, 0, 375)
    
  elif (mode == 'r'):
    if servo_drive <= 375 and servo_drive > 359:
      servo_drive = 375
    servo_drive = servo_drive + 10
    pwm.set_pwm(0, 0, servo_drive)

  elif (mode == 'f'):
    if servo_drive < 375 and servo_drive >= 359:
      servo_drive = 359
    servo_drive = servo_drive - 10
    pwm.set_pwm(0, 0, servo_drive)
    
  elif (mode == 'a'):
    pwm.set_pwm(1, 1, steering_left)
    
  elif (mode == 'c'):
    pwm.set_pwm(1, 1, steering_center)
    
  elif (mode == 'a'):
    pwm.set_pwm(1, 1, steering_right)
    
    
  elif (mode == 'q'):
    pwm.set_pwm(0, 0, servo_neutral)
    pwm.set_pwm(1, 1, steering_center)
    print('Good Bye')
    sys.exit()
    
  else: 
    print('No Command Try Again')
  time.sleep(0.1)
  
  
  
  

