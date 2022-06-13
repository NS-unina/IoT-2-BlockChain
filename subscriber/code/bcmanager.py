import sys
import time
import pprint

from web3.middleware import geth_poa_middleware
from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
from eth_tester import PyEVMBackend
from solcx import compile_source

class iot2blockchian:
    def __init__(self, rpcProvider = "http://172.11.0.66:8545"):
        self.w3 = Web3(Web3.HTTPProvider(rpcProvider))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract_interface = ""
        self.contract_id = ""
        self.address = ""
 

    def sendTransaction(self):
        pass

    def deploy_contract(self):
        def deploy_contract(w3, contract_interface):
            tx_hash = self.w3.eth.contract(
                abi=contract_interface['abi'],
                bytecode=contract_interface['bin']).constructor().transact({'from': w3.eth.accounts[0]})
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash) 
            #pprint.pprint(dict(receipt))
            address = self.w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
            return address
        
        self.address = deploy_contract(self.w3, self.contract_interface)
        print(f'[+] Deployed contract with address: {self.address}')

    def compile_source_file(self, file_path):
        with open(file_path, 'r') as f:
            source = f.read()
        compiled_sol = compile_source(source)
        self.contract_id, self.contract_interface = compiled_sol.popitem()

    def setTransaction(self, val):
        store_var_contract = self.w3.eth.contract(address=self.address, abi=self.contract_interface["abi"])
        tx_hash = store_var_contract.functions.setVar(val).transact({'from': self.w3.eth.accounts[0]})
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        #pprint.pprint(dict(receipt))
        if receipt["status"] == 1:
            print("[+] Transaction was successful")
