#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Klaus Herchenroder and  Ghansyam Patel
#Version: 3

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# PWM Adafruit Library
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096 
servo_max = 600  # Max pulse length out of 4096
servo_current = 375

# Helper function to make setting a servo pulse width simpler
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, for servos.
pwm.set_pwm_freq(60)

# To quit
print('Moving servo on channel 0, press Ctrl-C to quit...')

pwm.set_pwm(0, 0, servo_min)
time.sleep(1.0)
while True:
    if servo_current > servo_min:
        servo_current = servo_current - 0
        pwm.set_pwm(0, 0, servo_current)
        print("Current Servo Position: ", servo_current)
        time.sleep(0.5)
    else:
        pwm.set_pwm(0, 0, 375)
        break
      
    # Move servo on channel O between extremes.
    #pwm.set_pwm(0, 0, servo_min) # Servo will be on position 0
    #time.sleep(1) # 1 Second
    #pwm.set_pwm(0, 0, servo_neutral) # Servo will be on position 90
    #time.sleep(1) # 1 Second
    #pwm.set_pwm(0, 0, servo_max) # Servo will be on position 180
    #time.sleep(1) # 1 Second
    #pwm.set_pwm(0, 0, servo_neutral) # Servo will be on position 90
    #time.sleep(1) # 1 Second
    #pwm.set_pwm(0, 0, servo_min) # Servo will be on position 0
    #time.sleep(1) # 1 Second
