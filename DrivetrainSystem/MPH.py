#Accelrometer RPM to MPH simpler formula 

#Rahul Manoharan
#11/17/2016

import smbus
import time

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x08

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    rpm = bus.read_byte(address)
    return rpm

while True:
    var = 1
    writeNumber(var)
    time.sleep(1)

    rpm = readNumber()
    print ("Arduino: Here's the current RPM: "), rpm
    
    MPH = ( (4.5 * rpm) * 60) / 63360
    print ("Here's the current MPH: "), MPH
