#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung
import time
from grovepi import *

# Connect the Grove LED to digital port 04
led = 4

pinMode(led,"OUTPUT")
time.sleep(1)
while True:
	try:
		#Blink the LED
		digitalWrite(led,1)   # Send HIGH to switch LED
		time.sleep(1)
		
		digitalWrite(led,0)   # Send LOW to swtich off LED
		time.sleep(1)
	except KeyboardInterrupt:
		digitalWrite(led,0)   # Turn LED off before stopping
		break
	except IOError:
		print "Error"
