#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung

from grovepi import *
import RPi.GPIO as GPIO
import time

ultrasonic_ranger = 4# Insert ultrasonic_ranger to D4 on the grovepi
ultrasonic_ranger2 = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)#PWM'Pulse-width Modulation' puts pin 11 to 50Hz
p.start(9)
try:
    while True:
	# Read distance value from Ultrasonic
	distantf1=ultrasonicRead(ultrasonic_ranger)
	distantf2=ultrasonicRead(ultrasonic_ranger)
	distantf3=ultrasonicRead(ultrasonic_ranger)
        distantf =(distantf1+distantf2+distantf3)/3 #ultrasonicRead(ultrasonic_ranger)
	distantr1=ultrasonicRead(ultrasonic_ranger2)
	distantr2=ultrasonicRead(ultrasonic_ranger2)
	distantr3=ultrasonicRead(ultrasonic_ranger2)
	distantr =(distantr1+distantr2+distantr3)/3 #ultrasonicRead(ultrasonic_ranger)
        if distantf <= 50 or distantr <=50 :
            p.ChangeDutyCycle(6.7) #engage brake
        else:
            p.ChangeDutyCycle(9)#disengage brake
except KeyboardInterrupt:
    GPIO.cleanup()
    p.stop()
