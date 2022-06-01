#!/usr/bin/env python

"""
A single-process subscriber.

"""
import json
import sys
import paho.mqtt.subscribe as subscribe

HOST = 'localhost'
PORT = 1883
KEEPALIVE = 60  # in seconds


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode('utf8'))
    ts = payload.get('timestamp')
    value = payload.get('value')
    print(f"[{ts}] {value} -- {msg.topic}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        topic = sys.argv[1]

        # for more details, see:
        # https://github.com/eclipse/paho.mqtt.python#subscribe-1
        subscribe.callback(
            on_message, topic, hostname=HOST, port=PORT, keepalive=KEEPALIVE
        )

    else:
        print("USAGE: ./subscriber.py <topic>")