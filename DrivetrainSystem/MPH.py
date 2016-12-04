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
    number = bus.read_byte(address)
    return number

while True:
    var = input("enter a number:")
    writeNumber(var)
    print ("RPI: Hi Arduino, I sent you "), var
    time.sleep(1)

    number = readNumber()
    print ("Arduino: Here's the current RPM: "), number
    
    MPH = ( (4.5 * number) * 60) / 63360
    print ("Here's the current MPH: "), MPH