import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "dummy-data"

client_id = 'python-mqtt-{random.randint(0, 1000)}'
username = 'iot'
password = 'blockchain'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[+] Connected to MQTT Broker!")
        else:
            print("[-] Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect("172.11.0.123", port)
    return client

def dummy_data():
    return random.randrange(1,10)    

def publish(client):
    while True:
        time.sleep(5)
        result = client.publish(topic, dummy_data())
  
        status = result[0]  
        if status == 0:
            print(f"[+] Send to topic `{topic}`")
        else:
            print(f"[-] Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()