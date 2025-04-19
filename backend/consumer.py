import pika
import json
from config import RABBITMQ_URL
from fcm_service import send_notification_to_all
from threading import Thread
import time

def start_consumer():
    def callback(ch, method, properties, body):
        message = json.loads(body)
        print("Received from queue:", message)

        send_notification_to_all(
            title=message["title"],
            body=message["body"],
            data=message.get("data", {}),
            image_url=message.get("image_url"),
            action_url=message.get("action_url", "")
        )

    def run():
        while True:
            try:
                connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
                channel = connection.channel()
                channel.queue_declare(queue="notifications")
                channel.basic_consume(queue="notifications", on_message_callback=callback, auto_ack=True)
                print("📡 Waiting for messages...")
                channel.start_consuming()
                break  # Exit loop if connection is established and consuming starts
            except pika.exceptions.AMQPConnectionError:
                print("RabbitMQ not ready, retrying...")
                time.sleep(5)  # Wait before retrying

    Thread(target=run).start()
