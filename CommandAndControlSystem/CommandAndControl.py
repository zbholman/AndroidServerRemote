'''

Command & Control System
Written by: Matthew Smith, Anthony Curran, Elaine Tang, and Andrew Rooney.
This file is the source code for the Command & Control System, which serves as the brain of this automated vehicle.
Last Updated: 11/10/2016

'''

#Imports
import queue
import serial
import socket
from threading import Thread


#Handles the message queue
def msgQueue():
	while True:
		item = q.get() #Gets last message queued.	
		ser.write(item) #Writes it to the serial port, all devices will get this running on BAUD 9500)
		sendToMonitoringAndLogging(item) #Forwards message to sTMAL function.
		q.task_done() #Task done, what a champ.

#Send the message to monitoring and logging. Can use basic ports for this.
def sendToMonitoringAndLogging(message):
	host = socket.gethostname()
	port = 9001
	s = socket.socket()
	s.bind((host,port))
	s.listen(5)
	
	#Gets connection from Monitoring & Logging Client.
	conn, addr = s.accept()

	while True:
		#sends message
		conn.send(message.encode())

		data = conn.recv(1024).decode()
		print(data)
		break
	conn.close() 

#Main Loop for listening and blasting out messages.
def main():
	#Sets up a queue for messages
	q = Queue()
	t = Thread(target=msgQueue)
	t.daemon = True
	t.start()
	
	#Serial Port Listening and adding messages to the MsgQueue.
	ser = serial.Serial('/dev/ttyUSB0', 9500)
	while True:
		incMsg = ser.readline()
		print('Recieved: %s' % incMsg)
		q.put(incMsg)

if __name__ == "__main__":
    main()

