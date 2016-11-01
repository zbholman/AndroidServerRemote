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

# Import the PCA9685 module.
import Adafruit_PCA9685

# PWM Adafruit Library
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096 
servo_max = 600  # Max pulse length out of 4096
servo_neutral = 375

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
    print('Drive Mode:')
    mode = raw_input()
    pwm.set_pwm(0, 0, neutral) #Sets te car into neutral

    if(mode == 'p'): #Sets car into park, place holder code
	    print('Stop')
	    
    elif(mode == 's'): #Sets car into reverse at top speed
	    pwm.set_pwm(0, 0, servo_min)
	    
    elif(mode == 'w'): #Sets car into forward at top speed
	    pwm.set_pwm(0, 0, servo_max)
	    
    elif(mode == 'n'): #Sets car into neutral 
	    pwm.set_pwm(0, 0, srvo_neural)

    elif(mode == 'q'): #Exits gear shift
	    pwm.set_pwm(0, 0, neutral)
	    stop()
	    sys.exit()
    else: #If invalid command is entered
	    print('No Command try again')
	    time.sleep(0.1)

	    
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
