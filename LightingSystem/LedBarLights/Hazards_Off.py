import grovepi

# DI,DCKI,VCC,GND
leftledbar = 6
rightledbar = 5
grovepi.ledBar_init(leftledbar, 0)
grovepi.ledBar_init(rightledbar, 0)

grovepi.pinMode(rightledbar,"OUTPUT")
grovepi.pinMode(leftledbar,"OUTPUT")
i = 0
grovepi.ledBar_orientation(leftledbar, 0)
grovepi.ledBar_orientation(rightledbar, 0)
# ledbar_setLed(pin,led,state)
# led: which led (1-10)
# state: off or on (0,1)

# ledbar_setLevel(pin,level)
# level: (0-10)

for i in range(3, 10):
    grovepi.ledBar_setLed(leftledbar, i, 0)
    grovepi.ledBar_setLed(rightledbar, i, 0)
