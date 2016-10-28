import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Climate and Control System', durable=True)
print(' {*} Waiting for messages. To exit press Ctrl+C')

def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print("[x] Climate and Control System received")
        ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                     queue='Climate and Control System')

channel.start_consuming()
