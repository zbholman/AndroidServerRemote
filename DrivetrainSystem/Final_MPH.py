#Accelrometer RPM to MPH simpler formula 
#No Diameter needed
#Rahul Manoharan and Ghansyam Patel
#11/17/2016

import bluetooth
import smbus
import time
import os

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)

port = server_sock.getsockname()[1]

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x08

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

print "Waiting for connection on RFCOMM channel %d" % port 
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

while True:
    var = 1
    writeNumber(var)
    print ("RPI: Hi Arduino, I sent you "), var
    time.sleep(1)

    number = readNumber()
    print ("Arduino: Here's the current RPM: "), number
    
    MPH = ( (4.5 * number) * 60) / 63360
    print ("Here's the current MPH: "), MPH
