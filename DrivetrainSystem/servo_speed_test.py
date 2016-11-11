Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Klaus Herchenroder
#Version: 1

from __future__ import division
import time
import sys

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

pwm.set_pwm(0, 0, 375)
time.sleep(1.0)
print('W : Increase speed by 1')
print('S : Decrease speed by 1')
print('E : Increase speed by 10')
print('D : Decrease speed by 10')
print('Q : Exit')
while True:
	mode = raw_input()
	pwm.set_pwm(0, 0, servo_current)

	if(mode == 'w'):
		servo_current = servo_current + 1
		pwm.set_pwm(0, 0, servo_current)
		print('Servo Current Value = ', servo_current)
		
	elif(mode == 's'):
		servo_current = servo_current - 1
		pwm.set_pwm(0, 0, servo_current)
		print('Servo Current Value = ', servo_current)

	elif(mode == 'e'):
		servo_current = servo_current + 10
		pwm.set_pwm(0, 0, servo_current)
		print('Servo Current Value = ', servo_current)

	elif(mode == 'd'):
		servo_current = servo_current - 10
		pwm.set_pwm(0, 0, servo_current)
		print('Servo Current Value = ', servo_current)

	elif(mode == 'q'):
		pwm.set_pwm(0, 0, 375)
		print('Servo Current Value = ', servo_current)
		sys.exit()

	else:
		print('Invalid command. Try again')
		time.sleep(0.1)
