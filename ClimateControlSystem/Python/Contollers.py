#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#Controller.py
#Author: Nirav Patel

# Contoller.py is a python server script that waits for the connection from client via Bluetooth.
# Once the connection is esatablished a infinite loop is created that waits for incoming data from client.
# and than it process that data to turn on and off devices via relay.

# import statement for bletooth and GPIO pins.
import bluetooth
import RPi.GPIO as GPIO

#GPIO pins setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Server socket creation using Bluetooth Socket on Port 1.
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",1))
server_sock.listen(1)

port = server_sock.getsockname()[1]

#Server waitong for client to join on port 1/
print "Waiting for connection on RFCOMM channel %d" % port
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

# infinite loop unti the value is True
while True:
        # recieving data from the client side and storing in data variable.
        data=client_sock.recv(1024)        
        if data == "acON": #check if data recieved is equal to "acON" 
               GPIO.output(23,GPIO.LOW) #if its equal pin 23 is turn on which is attached to relay that turn on AC.
               print("AC ON")
        elif data == "acOFF": #check if data recieved is equal to "acOFF" 
               GPIO.output(23,GPIO.HIGH) #if its equal pin 23 is turn off which is attached to relay that turn off AC.
               print("AC OFF")
        elif data == "heatON": #check if data recieved is equal to "heatON" 
               GPIO.output(24,GPIO.LOW) #if its equal pin 24 is turn on which is attached to relay that turn on Heating Pad.
               print("HEAT ON")
        elif data == "heatOFF": #check if data recieved is equal to "heatOFF" 
               GPIO.output(24,GPIO.HIGH)#if its equal pin 24 is turn on which is attached to relay that turn off Heating Pad. 
               print("HEAT OFF")
        
#closing the server and client connection.
client_sock.close()
server_sock.close() 

