import pika 
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='drivetrain', durable=True)
print(' {*} Waiting for the messages. To exit press Ctrl+C')

def callback(ch, method, properties, body):
	print(" [x] Recieved %r" % body)
	time.sleep(body.count(b'.'))
	print("[x] DriveTrain system recieved")
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
			queue='drivetrain')

channel.start_consuming()
