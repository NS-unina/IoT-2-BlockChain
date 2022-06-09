# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
from mqttnode import publisher

def run():
    connector = publisher()
    connector.connect_mqtt()
    connector.client.loop_start()
    while True:
        time.sleep(5)
        connector.publish(random.randint(0,10))

if __name__ == '__main__':
    run()