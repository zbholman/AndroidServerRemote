#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Klaus Herchenroder
#Version: 4


from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# PWM Adafruit Library
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096 
servo_max = 600  # Max pulse length out of 4096
servo_neutral = 375 #The max pulse length of neutal
servo_drive = 400 #The value to be changed for speed


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

#pwm.set_pwm(0, 0, servo_min)
#time.sleep(1.0)

while True:
    print('Drive Mode:')
    mode = raw_input()
    pwm.set_pwm(0, 0, neutral) #Sets te car into neutral

    if(mode == 'p'): #Sets car into park, place holder code
	    print('Stop')
	    
    elif(mode == 's'): #Sets car into reverse
	    pwm.set_pwm(0, 0, servo_drive)
	    if servo_drive > 375:
		    servo_drive = servo_drive - (((359 - servo_drive) * 2) + 16)
	    pwm.set_pwm(0, 0, servo_drive)
	    
    elif(mode == 'w'): #Sets car into drive
	    if servo_drive < 359:
		    servo_drive = servo_drive + (((359 - servo_drive) * 2) + 16)
	    pwm.set_pwm(0, 0, servo_drive)
	    
    elif(mode == 'n'): #Sets car into neutral 
	    pwm.set_pwm(0, 0, 375)
	    
    elif(mode == 't'): #Speeds up the car
	    if servo_drive <= 375 && servo_drive > 359:
		    servo_drive = 375
	    servo_drive = servo_drive + 10
	    pwm.set_pwm(0, 0, servo_drive)

    elif(mode == 'g'): #Speeds down the car
	    if servo_drive < 375 && servo_drive >= 359:
		    servo_drive = 359
	    servo_drive = servo_drive - 10
	    pwm.set_pwm(0, 0, servo_drive)

    elif(mode == 'f'): #Emergency Stop
	    if servo_drive != 375:
		    servo_drive = 375

    elif(mode == 'q'): #Exits gear shift
	    pwm.set_pwm(0, 0, neutral)
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

