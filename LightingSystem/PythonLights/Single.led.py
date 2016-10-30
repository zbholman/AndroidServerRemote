import time
import grovepi
import random

# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
ledbar = 5

grovepi.pinMode(ledbar,"OUTPUT")
time.sleep(1)
i = 0
for i in range(0,1):
            grovepi.ledBar_setBits(ledbar, i)
            time.sleep(.2)
"""
while True:
    try:
        print ("Test 18) Walk through all possible combinations")
        for i in range(0,1):
            grovepi.ledBar_setBits(ledbar, i)
            time.sleep(.2)
        time.sleep(.1)
"""
        
    except KeyboardInterrupt:
         grovepi.ledBar_setBits(ledbar, 0)
         break
    except IOError:
         print ("Error") 
