import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pin = 4

# loop through pins and set mode and state to 'high'

GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 10

# main loop

try:
  GPIO.output(4, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

