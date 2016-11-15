import bluetooth
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)



server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",1))
server_sock.listen(1)

port = server_sock.getsockname()[1]
print "Waiting for connection on RFCOMM channel %d" % port
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info
while True:	        	
	data = client_sock.recv(1024)

	if (data == "0"):
		print ("LED OFF")
		GPIO.output(23,GPIO.HIGH)
	elif (data == "1"):
		print ("LED ON")
		GPIO.output(23,GPIO.LOW)
 	elif (data == "msg"):
		data = str("hi") + "!"

	client_sock.send(data)
	print ("sending %s " % data)
	
client_sock.close()
server_sock.close()
