#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)#removes warning about pin being in use
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)#puts pin 11 at 50Hz
p.start(9)

loopStart =  time.time()#time when program starts
timePassed = 0.0
try:
        while timePassed < 4:
                now = time.time()#current time
                timePassed = now - loopStart#current time minus time program started
                timePassed = int(timePassed)#changes timePassed into Integer
                p.ChangeDutyCycle(13.5)#engages brake
                time.sleep(0.125)#time between brake pumps
                p.ChangeDutyCycle(9)#disengages brake
                time.sleep(0.125)
        if timePassed >= 4:
                p.stop()#stops power to servo after 4 seconds
                GPIO.cleanup()

except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
        print ("I/O error({0}): {1}".format(e.errno, e.strerror)
