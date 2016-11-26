import grovepi

# DI,DCKI,VCC,GND
ledbar = 6

grovepi.ledBar_init(ledbar, 0)
grovepi.pinMode(ledbar,"OUTPUT")
i = 0
grovepi.ledBar_orientation(ledbar, 0)

# ledbar_setLed(pin,led,state)
# led: which led (1-10)
# state: off or on (0,1)

# ledbar_setLevel(pin,level)
# level: (0-10)

for i in range(3, 10):
    grovepi.ledBar_setLed(ledbar, i, 0)
