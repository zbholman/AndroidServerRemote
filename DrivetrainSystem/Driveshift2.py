#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Ivan Iakimenko, Klaus Herchenroder, and Ghansyam Patel
#Version: 6


from __future__ import division
from ArduinoServo import ServoControl
import time
import sys

Servo = ServoControl()

# Configure min and max servo pulse lengths
servo_min = 0  # Min pulse length out of 4096 
servo_max = 180  # Max pulse length out of 4096
servo_neutral = 90 #The max pulse length of neutal
servo_drive = servo_neutral #The value to be changed for speed

# To quit
print('press Ctrl-C to quit...')
print("w = forward")
print("a = turn left")
print("s = reverse")
print("d = turn right")
print("n = neutral")
print("p = park")
print("f = increase speed")
print("g = decrease speed")
print("c = center steering")

while True:
    print"Drive Mode:",
    mode = raw_input()

    if (mode == 'p'): #Sets car into park, place holder code
	print('Stop')
	Servo.setGas(servo_neutral)
		
    elif (mode == 's'): #Sets car into reverse
        Servo.setGas(servo_neutral)
	#if servo_drive > servo_neutral:
            #servo_drive = servo_drive - (((servo_drive - 375) * 2) + 16)
        servo_drive = 88
	Servo.setGas(servo_drive)
	    
    elif (mode == 'w'): #Sets car into drive
        Servo.setGas(servo_neutral)
	#if servo_drive < 359:
            #servo_drive = servo_drive + (((359 - servo_drive) * 2) + 16)
        servo_drive = 92
	Servo.setGas(servo_drive)
	    
    elif (mode == 'n'): #Sets car into neutral 
	Servo.setGas(servo_neutral)
	    
    elif (mode == 'f'): #Speeds up the car
	if servo_drive <= servo_neutral or servo_drive >= servo_max:
            servo_drive = servo_neutral
	servo_drive = servo_drive + 1
	Servo.setGas(servo_drive)
	    
    elif (mode == 'g'): #Slows down the car
	if servo_drive <= servo_neutral:
	    servo_drive = servo_neutral
	servo_drive = servo_drive - 1
	Servo.setGas(servo_drive)

    elif (mode == 'a'): #Turns the car left
        Servo.setSteering(servo_max)

    elif (mode == 'c'): #Sets the steering to center
        Servo.setSteering(servo_neutral)
			
    elif (mode == 'd'): #Turns the car right
        Servo.setSteering(servo_min)
	    
    elif (mode == 'q'): #Exits gear shift
	Servo.setGas(servo_neutral)
	Servo.setSteering(servo_neutral)
	print('Good Bye')
	sys.exit()
	    
	    
    else: #If invalid command is entered
	print('No Command try again')
    
    time.sleep(0.1)
