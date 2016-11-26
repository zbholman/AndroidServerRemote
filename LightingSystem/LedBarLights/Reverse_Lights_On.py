import grovepi

# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
rightledbar = 5
leftledbar = 6

grovepi.pinMode(rightledbar,"OUTPUT")
grovepi.pinMode(leftledbar,"OUTPUT")

# ledbar_setLed(pin,led,state)
# led: which led (1-10)
# state: off or on (0,1)

grovepi.ledBar_setLed(rightledbar, 2, 1)
grovepi.ledBar_setLed(leftledbar, 2, 1)
