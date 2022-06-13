from web3 import Web3  
from web3.middleware import geth_poa_middleware
import time

contractAddress = '0xF7efDaE8b2Fd2183B6E98b5F294386DFDfc7eBC2'
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

f = open("abi.txt", "r")
abi2 = f.read()

contract = w3.eth.contract(address=contractAddress, abi=abi2)
accounts = w3.eth.accounts
greeting_Event = contract.events.MyEvent() # Modification

def handle_event(event):
    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    result = greeting_Event.processReceipt(receipt) # Modification
    print(result[0]['args'])

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
            time.sleep(poll_interval)

block_filter = w3.eth.filter({'fromBlock':'latest', 'address':contractAddress})
log_loop(block_filter, 2)