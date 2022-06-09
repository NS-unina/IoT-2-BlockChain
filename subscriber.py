# python3.6

import random

from web3 import Web3
from web3.middleware import geth_poa_middleware

from paho.mqtt import client as mqtt_client
from mqttnode import subscriber


broker = '127.0.0.1'
port = 1883
topic = "dummy-data"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def main():

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    connector = subscriber()
    connector.connect_mqtt()
    connector.subscribe()
    connector.loop_forever()


if __name__ == '__main__':
    main()