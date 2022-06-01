#!/usr/bin/env python

"""
Spawn a lot of publishers.

"""
import json
import os
import random
import sys
import paho.mqtt.client as mqtt

from datetime import datetime
from multiprocessing import Process


HOST = 'localhost'
PORT = 1883
KEEPALIVE = 60  # in seconds


# This callback is called when a message that was to be sent using the publish()
# call has completed transmission to the broker.
def on_publish(client, userdata, mid):
    print(f"Client: {client.spawned_from_pid} published message: {mid}")


def _get_data(pid):
    ts = datetime.utcnow().strftime("%c")
    value = random.random()
    print(f"Publishing [{ts}] {value} from {pid}")
    return json.dumps({'timestamp': ts, 'value': value, 'pid': pid})


def spawn_client(topic="default"):
    pid = os.getpid()
    print(f"Creating client with PID: {pid}")
    client = mqtt.Client()
    client.spawned_from_pid = pid
    client.connect(HOST, PORT, KEEPALIVE)
    client.on_publish = on_publish
    client.loop_start()
    try:
        while True:
            client.publish(topic, payload=_get_data(pid), qos=0, retain=False)
    except KeyboardInterrupt:
        print(f"Calling loop_stop() for pid: {pid}")
        client.loop_stop()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        topic = sys.argv[1]
        try:
            n_procs = int(sys.argv[2])
        except (ValueError, IndexError):
            n_procs = 4

        procs = []
        for _ in range(n_procs):
            p = Process(target=spawn_client, args=(topic, ))
            p.start()
            procs.append(p)
        # do I need to call .join() if I dont' care about return values?
        for p in procs:
            p.join()
    else:
        print("USAGE: ./publishers <topic> [n_processes]")