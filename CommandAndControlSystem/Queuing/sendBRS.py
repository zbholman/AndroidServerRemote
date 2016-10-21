#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='braking', durable=True)

message = ' '.join(sys.argv[1:]) or "Braking System"
channel.basic_publish(exchange='',
		      routing_key='braking',
		      body=message,
		      properties=pika.BasicProperties(
		      	delivery_mode = 2, # make message persistent
		      ))

print(" [x] Sent %r" % message)
connection.close()

