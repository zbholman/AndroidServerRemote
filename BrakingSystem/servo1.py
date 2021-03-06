#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		time.sleep(0.25)
		p.ChangeDutyCycle(12.5)
		time.sleep(0.25)
	#	p.ChangeDutyCycle(7.5)
	#	time.sleep(0.1)
	#	p.ChangeDutyCycle(12.5)
	#	time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
