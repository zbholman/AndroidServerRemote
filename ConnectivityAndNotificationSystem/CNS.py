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

#Send the message to monitoring and logging. Can use basic ports for this.
def sendToNotification(message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='Notifications System', durable=True)

	message = ' '.join(sys.argv[1:]) or "Notifications System"
	channel.basic_publish(exchange='',
                     	 routing_key='Notifications System',
                     	 body=message,
                     	 properties=pika.BasicProperties(
                	        delivery_mode = 2, # make message persistent
        	              ))
	print(" [x] Sent %r" % message)
connection.close()
