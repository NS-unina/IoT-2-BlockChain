import random

from bcmanager import iot2blockchian

from paho.mqtt import client as mqtt_client
from mqttnode import subscriber

def main():
    web3 = iot2blockchian()
    contract_source_path = './contracts/storage.sol'
    web3.compile_source_file(contract_source_path)
    web3.deploy_contract()
    
    connector = subscriber()
    connector.connect_mqtt()
    connector.subscribe(web3)
    connector.loop_forever()

if __name__ == '__main__':
    main()