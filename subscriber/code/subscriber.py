import random

from bcmanager import iot2blockchian

from paho.mqtt import client as mqtt_client
from mqttnode import subscriber
import time

def main():
    print("[+] Start script")
    time.sleep(10)
    print("[+] End sleep")
    web3 = iot2blockchian()
    print("[+] Attach to geth")
    contract_source_path = './contracts/storage.sol'
    web3.compile_source_file(contract_source_path)
    web3.deploy_contract()
    
    connector = subscriber()
    connector.connect_mqtt()
    connector.subscribe(web3)
    connector.loop_forever()

if __name__ == '__main__':
    main()