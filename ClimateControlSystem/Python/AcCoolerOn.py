#import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [22]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i,0)

def trigger() :
        for i in pinList: 
          GPIO.output(i,0)
#         GPIO.cleanup()
          break
     
try: 
	trigger()
         
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
