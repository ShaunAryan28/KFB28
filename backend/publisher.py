import pika
import json
import time
from config import RABBITMQ_URL

def publish_message(message: dict):
    while True:
        try:
            # Try to establish a connection to RabbitMQ
            connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
            channel = connection.channel()
            channel.queue_declare(queue="notifications")
            channel.basic_publish(
                exchange='',
                routing_key="notifications",
                body=json.dumps(message)
            )
            connection.close()
            print("Message published successfully")
            break  # Exit the loop if the message was successfully published
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready, retrying...")
            time.sleep(5)  # Wait before retrying
