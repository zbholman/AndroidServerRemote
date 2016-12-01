import time
import grovepi
import sys

# DI,DCKI,VCC,GND
ledbar = 6

grovepi.ledBar_init(ledbar, 0)
grovepi.pinMode(ledbar,"OUTPUT")
i = 0
grovepi.ledBar_orientation(ledbar, 1)

# ledbar_setLed(pin,led,state)
# led: which led (1-10)
# state: off or on (0,1)

# ledbar_setLevel(pin,level)
# level: (0-10)

while True:
    try:
        for i in range(0, 9):
            grovepi.ledBar_setLed(ledbar, i, 1)
            time.sleep(.2)

        for i in range(0, 9):
            grovepi.ledBar_setLed(ledbar, i, 0)
            time.sleep(.2)

    except (KeyboardInterrupt, SystemExit):
        for i in range(0, 9):
            grovepi.ledBar_setLed(ledbar, i, 0)
        sys.exit(-1)
