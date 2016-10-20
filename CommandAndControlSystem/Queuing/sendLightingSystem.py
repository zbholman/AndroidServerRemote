#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='lighting')

channel.basic_publish(exchange='',
                      routing_key='lighting',
                      body='Activate right turn signal')
print(" [x] Sent 'right turn signal request'")
connection.close()
