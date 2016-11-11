'''

Command & Control System
Written by: Matthew Smith, Anthony Curran, Elaine Tang, and Andrew Rooney.
This file is the source code for the Command & Control System, which serves as the brain of this automated vehicle.
Last Updated: 11/10/2016

'''

#Imports
import serial
from threading import Thread
import queue

#Handles the message queue
def msgQueue():
	while True:
		item = q.get() #Gets last message queued.
	
		ser.write(item) #Writes it to the serial port, all devices will get this running on BAUD 9500)
		sendToMonitoringAndLogging(item) #Forwards message to sTMAL function.
		q.task_done() #Task done, what a champ.

#Send the message to monitoring and logging. Can use basic ports for this.
def sendToMonitoringAndLogging(message):
	#Finish this. They will just be another .py on our own system, so use basic socket programming. I have the code for this and can send this to you. Really simple. 
	
#Main Loop for listening and blasting out messages.
def main():

	#Sets up a queue for messages
	q = Queue()
        t = Thread(target=msgQueue)
        t.daemon = True
        t.start()
		

	ser = serial.Serial('/dev/ttyUSB0', 9500)
	incMsg = ser.readline()
	print('Recieved: %s' % incMsg)
	q.put(incMsg)
