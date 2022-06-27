# python 3.6
import argparse
import random
import time

from paho.mqtt import client as mqtt_client
from mqttnode import publisher

def main(topic, id):
    connector = publisher("172.11.0.123", 1883, topic, id)
    connector.connect_mqtt()
    connector.client.loop_start()
    while True:
        time.sleep(5)
        connector.publish(random.randint(0,10))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IoT demo device')
    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument('-t', '--topic', help='name of MQTT topic', required=True)
    required_named.add_argument('-i', '--id', help='device ID', required=True)
    args = parser.parse_args()
    
    main(args.topic, args.id)