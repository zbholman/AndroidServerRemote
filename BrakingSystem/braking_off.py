#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)#

p = GPIO.PWM(11,50)#PWM'Pulse-width Modulation' puts pin 11 to 50Hz
p.start(5)
loopStart =  time.time()   #time when program starts
timePassed = 0.0
try:
        while timePassed < 2:
                now = time.time()   #current time
                timePassed = now - loopStart   #current time minus time program started
                timePassed = int(timePassed)   #changes timePassed into Integer
		p.ChangeDutyCycle(9)#disengage brakes after 2 seconds
		if timePassed >= 4 :
			p.stop()   #stops power to servo after 4 seconds
			GPIO.cleanup()
except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
#while True :
#	p.ChangeDutyCycle(9)#disengage brakes after 2 seconds
#p.stop()#stops power to servo
#GPIO.cleanup()
