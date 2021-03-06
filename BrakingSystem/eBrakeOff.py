#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)#PWM'Pulse-width Modulation' puts pin 11 to 50Hz
p.start(7)

try:
    p.ChangeDutyCycle(10) #disengage emergency brake
  # p.ChangeDutyCycle(10) #disengage emergency brake
  # p.ChangeDutyCycle(10) #disengage emergency brake
  #  GPIO.cleanup()
  #  p.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
    p.stop()
