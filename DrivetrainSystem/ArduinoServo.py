#ArduinoServo.py
#Written by Ivan Iakimenko
#Version 1

import smbus
import time

bus = smbus.SMBus(1)

class ServoControl (object):

    address = 0x07
    G = 200
    S = 201

    def __init__(self):
        pass
        
    def setSteering(self, value):
        bus.write_byte(self.address, self.S)
        bus.write_byte(self.address, value)
        
    def setGas(self, value):
        bus.write_byte(self.address, self.G)
        bus.write_byte(self.address, value)
