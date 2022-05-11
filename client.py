import random
import time
import pika

value = 5


def noiseGenerator(): 
    return random.randint(-1, 1)


def main():
    global value
    while True:  
        value = value + noiseGenerator()
        time.sleep(1)
        print(value)

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
    main()