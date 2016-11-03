#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung

from grovepi import *
import RPi.GPIO as GPIO
import time

ultrasonic_ranger = 4  # Insert ultrasonic_ranger to D4 on the grovepi
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)#PWM'Post-width Modulation' puts pin 11 to 50Hz
p.start(9)

while True:
    try:
        # Read distance value from Ultrasonic
        distant = ultrasonicRead(ultrasonic_ranger)
        if distant <= 50:
            p.ChangeDutyCycle(13.5)#engage brake
        else:
            p.ChangeDutyCycle(9)#engage brake

    except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
