import pika
import time

#Creates a connection using pika with a Parameters of setting host equal to 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
#Is a primary communication method for interacting with RabbitMQ
channel = connection.channel()
#Declares the queue and name it 'Monitoring and Logging'
channel.queue_declare(queue='Monitoring and Logging', durable=True)
#Print message out to the user telling them how to close the connection and the channel
print(' {*} Waiting for messages. To exit press Ctrl+C')

#Callback function that will be called when message is sent via the connection
def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print("[x] Monitoring and Logging received")
        ch.basic_ack(delivery_tag = method.delivery_tag)

#Recieves a maximum of 1 message at once
channel.basic_qos(prefetch_count=1)
#Consumers recieve new messages when the limit on messages has been reached
channel.basic_consume(callback,
                     queue='Monitoring and Logging System')
#Starts server to listen for messages until the consumers are cancelled
channel.start_consuming()

