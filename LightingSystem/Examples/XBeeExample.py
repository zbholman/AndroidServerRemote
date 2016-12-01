# Author: Brian Holman
# Course: IST 440
# Team: LightingSystem
# Date: 10-02-2016

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
string = raw_input('What to send to XBee: ')
print ('Sending "%s"' % string)
ser.write('%s\n' % string)
