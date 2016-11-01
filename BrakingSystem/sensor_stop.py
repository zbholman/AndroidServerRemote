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
        d = str(distant)
        if distant <= 50:
            time.sleep(10)  # sleep time added
        elif distant <= 15:
            setText("Getting a little too Close " + d + " cm")
        else:
            setText("Dist = " + d + " cm")

except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
