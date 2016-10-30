import time
from grovepi import *

# Connect the Grove LED to digital port D5
led = 5

pinMode(led,"OUTPUT")
time.sleep(1)

print ("This example will blink a Grove LED connected to the GrovePi+ on the port labeled D5.\nIf you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.\nYou may also try reversing the direction of the LED on the sensor.")
print (" ")
print ("Connect the LED to the port labele D5!" )

while True:
    try:
        #Blink the LED
        digitalWrite(led,1)		# LED turned on
        print ("LED ON!")
        time.sleep(2)

        digitalWrite(led,0)		# LED turned off 
        print ("LED OFF!")
        time.sleep(2)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:				# Print "Error" if communication error encountered
        print ("Error")
