# create CNS class that takes in data
# transfer data via CNS transfer mathod to notifactions
# due by tuesfer

from queue import *
import pika
import sys
from threading import *

#Handles the message queue
def msgQueue():
	while True:
		item = q.get() #Gets last message queued.
		if item is None:
			break	
		ser.write(item) #Writes it to the serial port, all devices will get this running on BAUD 9500)
		sendToNotification(item) #Forwards message to sTMAL function.
q.task_done() #Task done, what a champ.


