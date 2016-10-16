Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#IST 440
# Drive Train (Team 02)
# Author: Ghansyam Patel, Rahul Manoharan, and Klaus 
# Version: 1.02
# Date: 09/30/2016
#GoPiGo Robot for DriveTrain
from gopigo import *
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(2.5)

#Displays the Start Up Screen
print('Welcome to the DriveTrain System')
print('Press:')
print('p to Park the Car')
print('r to Reverse the Car')
print('n to Neutral')
print('d to Drive the Car')
print('l to Move the Car Left')
print('r to Move the Car Right')
print('i to Increase the Speed')
print('e to Decrease the Speed')
print('z to Exit the Drive Mode')

car = '    ______'
car1= '  /___ __\\___'
car2= '   o-----o    '

while True:
    print"Drive Mode:",
    mode = raw_input()
    if (mode == 'p'):
        stop()  #Car In The Park Mode
        
    elif (mode == 'r'):
	p.ChangeDutyCycle(2.5)  # turn towards 0 degree
	time.sleep(1) # sleep 1 second
        bwd() #Car Reversing
        
    elif (mode == 'n'):
	p.ChangeDutyCycle(7.5)  # turn towards 90 degree
	time.sleep(1) # sleep 1 second
        stop()  #Car In The Neutral Mode
        
    elif (mode == 'd'):
	p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second
        fwd() #Car Moving Forward

    elif (mode == 'l'):
        left() #Car Turning Left

    elif (mode == 't'):
        right() #Car Turning Right

    elif (mode == 'i'):
        increase_speed() #Increasing The Car Speed

    elif (mode == 'e'):
        decrease_speed() #Car Turning Left

    elif (mode == 'z'):
        stop() #Car Stops before Exiting Drive Mode
        print('Exiting Drive Mode') #Leaving Drive Mode
        print(car) #Printing Car
        print(car1) #Printing Car
        print(car2) #Printing Car
        print('Good Bye!') #Exiting Message!
        sys.exit()
    else:
        print('Wrong Drive Mode Command, Please Try Again')
    time.sleep(.1)

#Original Servo Code

#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(12, GPIO.OUT)

#p = GPIO.PWM(12, 50)

#p.start(2.5)

#try:
#        while True:
#		p.ChangeDutyCycle(2.5)  # turn towards 0 degree
#		time.sleep(1) # sleep 1 second
#		p.ChangeDutyCycle(7.5)  # turn towards 90 degree
#		time.sleep(1) # sleep 1 second
#		p.ChangeDutyCycle(12.5) # turn towards 180 degree
#               time.sleep(1) # sleep 1 second
                
#except KeyboardInterrupt:
#	p.stop()
#        GPIO.cleanup()
