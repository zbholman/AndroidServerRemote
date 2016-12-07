'''Command & Control System
Written by: Anthony Curran, Elaine Tang, Andrew Rooney, and Matt Smith
This file is the source code for the Command & Control System, which serves as the brain of this automated vehicle.
Last Updated: 11/10/2016
'''

#Imports
import serial
import pika
import sys
import threading
from Queue import Queue
import logging



#logging.warning('Watch out!')  # will print a message to the console
#logging.info('I told you so')  # will not print anything
#Handles the message queue

def msgQueue(ser, q):
        while True:
                item = q.get() #Gets last message queued.
                if item is None:
                        break
                ser.write(item) #Writes it to the serial port, all devices will get this running on BAUD 9500)
                sendToMonitoringAndLogging(item) #Forwards message to sTMAL function.
                q.task_done() #Task done, what a champ.
		break

#Send the message to monitoring and logging. Can use basic ports for this.
def sendToMonitoringAndLogging(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='Command and Control System', durable=True)

        message = ' '.join(sys.argv[1:]) or "Command and Control System"
        channel.basic_publish(exchange='',
                         routing_key='Command and Control System',
                         body=message,
                         properties=pika.BasicProperties(
                                delivery_mode = 2, # make message persistent
                              ))
        print(" [x] Sent %r" % message)
        connection.close()

#Main Loop for listening and blasting out messages.
def main():
	
	#Serial Port Listening and adding messages to the MsgQueue.
	ser = serial.Serial('/dev/ttyUSB0', 9500)
	
	q = Queue(maxsize=5)
	
	t = threading.Thread(target=msgQueue(ser,q))
	t.daemon = True
	
	print('Queue and Thread done')
        while True:
                try:
			print('i hurd u bihh')    
                        incMsg = ser.readline()
                        print('Recieved: %s' % incMsg)
                        q.put(incMsg)
			t.start()
			t.join()
                except(RuntimeError, OSError, ValueError, IOError) as e:
                        print('Error:' + str(e))
                        break

if __name__ == "__main__":
	main()
