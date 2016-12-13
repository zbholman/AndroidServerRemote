#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)#PWM'Pulse-width Modulation' puts pin 11 to 50Hz
p.start(9)
try :
	while True :
		p.ChangeDutyCycle(5)#engage brake
except KeyboardInterrupt:
	exit()
