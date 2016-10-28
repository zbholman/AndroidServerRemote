import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Climate and Control System', durable=True)

message = ' '.join(sys.argv[1:]) or "Climate and Control System"
channel.basic_publish(exchange='',
                      routing_key='Climate and Control System',
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode = 2, # make message persistent
                      ))

print(" [x] Sent %r" % message)
connection.close()

