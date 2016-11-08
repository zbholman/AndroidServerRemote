import time
import grovepi
import random

# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
ledbar = 5

grovepi.pinMode(ledbar,"OUTPUT")
i = 0

while True:
    try:
        # ledbar_setLed(pin,led,state)
        # led: which led (1-10)
        # state: off or on (0,1)

        # green to red
        grovepi.ledBar_orientation(ledbar, 1)
        time.sleep(.5)

        print ("Test 2) Set level")
        # ledbar_setLevel(pin,level)
        # level: (0-10)

        for i in range(0, 9):
            grovepi.ledBar_setLed(ledbar, i, 1)
            time.sleep(.2)

        for i in range(0, 9):
            grovepi.ledBar_setLed(ledbar, i, 0)
            time.sleep(.2)


    except KeyboardInterrupt:
        grovepi.ledBar_setBits(ledbar, 0)
        break
    except IOError:
        print ("Error")
