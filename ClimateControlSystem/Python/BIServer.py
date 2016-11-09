import os
import glob
import time
import RPi.GPIO as GPIO
import bluetooth
from bluetooth import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "00001101-0000-1000-8000-00805F934FBB"

bluetooth.advertise_service( server_sock, "AquaPiServer",uuid )
while True:          
	print "Waiting for connection on RFCOMM channel %d" % port

	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info

	try:
	        data = client_sock.recv(1024)
        	if len(data) == 0: break
	        print "received [%s]" % data

		if data == 'lightOn':
			GPIO.output(23,False)
			data = 'light on!'
		elif data == 'lightOff':
			GPIO.output(23,True)
			data = 'light off!'
		else:
			data = 'WTF!' 
	        client_sock.send(data)
		print "sending [%s]" % data

	except IOError:
		pass

	except KeyboardInterrupt:

		print "disconnected"

		client_sock.close()
		server_sock.close()
		print "all done"

		break
