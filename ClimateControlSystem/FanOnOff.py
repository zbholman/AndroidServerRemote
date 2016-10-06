#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeS = 5

# main loop

try:
  while True:

    for i in pinList:
      GPIO.output(i, GPIO.LOW)
      print("ON")
      time.sleep(SleepTimeS);

    for i in pinList:
      GPIO.output(i, GPIO.HIGH)
      print("OFF")
      time.sleep(SleepTimeS);
      
    pinList.reverse()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

