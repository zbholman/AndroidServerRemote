# Raspberry Pi + Grove Switch + Grove Relay

import time
import grovepi

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND

relay = 4

grovepi.pinMode(relay,"OUTPUT")

grovepi.digitalWrite(relay,1)
