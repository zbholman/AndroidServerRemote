#!/usr/bin/env python
import pika
import sys

connection = pika.BlockConnection(pika.ConnectionParameters(
	host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='drivetrain', durble=True)

message = ' '.join(sys.argv[1:]) or "DriveTrain System"
channel.basic_publish(exchange='',
			routing_key='drivetrain',
			body=message,
			properties=pika.BasicProperties(
			  delivery_mode = 2, 
			))

print(" [x] Sent 'Move vehicle'" % message:)
connection.close()
