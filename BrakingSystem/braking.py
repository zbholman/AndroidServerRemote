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

p = GPIO.PWM(11,50)#PWM'Post-width Modulation' puts pin 11 to 50Hz
p.start(9)

loopStart =  time.time()#time when program starts
timePassed = 0.0
try:
        while timePassed < 2:
                now = time.time()#current time
                timePassed = now - loopStart#current time minus time when program started
                timePassed = int(timePassed)#makes timePassed into integer
		p.ChangeDutyCycle(13.5)#engage brake
		if timePassed == 2:
                	p.ChangeDutyCycle(9)#disengage brakes after 2 seconds
                if timePassed > 2:
                        p.stop()#stops power to servo
                        GPIO.cleanup()

except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
