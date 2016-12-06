'''Command & Control System
Written by: Matthew Smith, Anthony Curran, Elaine Tang, and Andrew Rooney.
This file is the source code for the Command & Control System, which serves as the brain of this automated vehicle.
Last Updated: 11/10/2016
'''

#Imports
import serial
import pika
import sys
import thread
import Queue
import logging

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
#Handles the message queue
def msgQueue():
        while True:
                item = q.get() #Gets last message queued.
                if item is None:
                        break
                ser.write(item) #Writes it to the serial port, all devices will get this running on BAUD 9500)
                sendToMonitoringAndLogging(item) #Forwards message to sTMAL function.
                q.task_done() #Task done, what a champ.

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
        while True:
                try:
                        #Serial Port Listening and adding messages to the MsgQueue.
                        ser = serial.Serial('/dev/ttyUSB0', 9500)
                        #Sets up a queue and thread for messages
                        q = Queue(maxsize=5)
                        t = Thread(target=msgQueue)
                        t.daemon = True
                        t.start()
                        

                        incMsg = ser.readline()
                        print('Recieved: %s' % incMsg)
                        q.put(incMsg)
                except(RuntimeError, OSError, ValueError, IOError) as e:
                        print('Error:' + str(e))
                        break

if __name__ == "__main__":
        main()

                                                                                                                      
