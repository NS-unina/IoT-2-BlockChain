# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
from mqttnode import publisher

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    connector = publisher()
    connector.connect_mqtt()
    connector.client.loop_start()
    while True:
        time.sleep(5)
        connector.publish(random.randint(0,10))

if __name__ == '__main__':
    run()