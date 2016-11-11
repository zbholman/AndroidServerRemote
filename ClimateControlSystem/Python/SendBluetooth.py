#Python code to test a client in socket programming

import socket

#create the socket object
socket_client = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

#Create host and port
host = ''
port = 1

socket_client.connect((host, port))
socket_client.send("FILE FROM CLIENT")
