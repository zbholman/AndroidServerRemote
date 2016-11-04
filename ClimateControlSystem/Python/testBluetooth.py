import bluetooth
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
  
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_sock.bind(("",port))
server_sock.listen(1)
 
client_sock,address = server_sock.accept()
print "Accepted connection from ",address
while True:
	data = client_sock.recv(1024)
 	print "received [%s]" % data
 	if (data == "0"):
	 	print ("Fan OFF")
 		GPIO.output(23,GPIO.HIGH)
 	if (data == "1"):
	 	print ("Fan ON")
 		GPIO.output(23,GPIO.LOW)
 		
 
client_sock.close()
server_sock.close()
