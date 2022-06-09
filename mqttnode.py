import random
from paho.mqtt import client as mqtt_client

class mqtt:
    client = ""

    def __init__(self, broker = "127.0.0.1", port = 1883, topic = "dummy-data", client_id = f'python-mqtt-{random.randint(0, 100)}'):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("[+] Connected to MQTT Broker!")
            else:
                print("[-] Failed to connect, return code %d\n", rc)
        
        self.client = mqtt_client.Client(self.client_id)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        
    
class publisher(mqtt):
    def __init__(self, broker = "127.0.0.1", port = 1883, topic = "dummy-data", client_id = f'python-mqtt-{random.randint(0, 100)}'):
        super().__init__(broker, port, topic, client_id)

    def loop_start(self):
        self.client.loop_start()


    def publish(self, dummy_data):   
        result = self.client.publish(self.topic, dummy_data)
        status = result[0]  
        if status == 0:
            print(f"[+] Send to topic {self.topic}")
        else:
            print(f"[-] Failed to send message to topic {self.topic}")

class subscriber(mqtt):
    def __init__(self, broker = "127.0.0.1", port = 1883, topic = "dummy-data", client_id = f'python-mqtt-{random.randint(0, 100)}'):
        super().__init__(broker, port, topic, client_id)

    def subscribe(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self.client.subscribe(self.topic)
        self.client.on_message = on_message

    def loop_forever(self):
        self.client.loop_forever()