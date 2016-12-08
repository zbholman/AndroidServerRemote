import time

from xbee import XBee
import serial

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

#Open serial API
ser = serial.Serial(PORT, BAUD_RATE)

#Create API object
xbee = XBee(ser, escaped=True)
import pprint
pprint.pprint(xbee.api_commands)

DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x81\x36\x75"

#Continuously read and print packets
while True:
   try:
	print "send data"
	xbee,tx_long_addr(frame='0x1', dest_addr=DEST_ADDR_LONG, data='AB')
	time.sleep(1)
   except KeyboardInterrupt:
	break

ser.close()
