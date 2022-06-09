import sys
import time
import pprint

from web3.middleware import geth_poa_middleware
from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
from eth_tester import PyEVMBackend
from solcx import compile_source

class iot2blockchian:
    def __init__(self, rpcProvider = "http://127.0.0.1:8545"):
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
        print(f'[+] Deployed contract with address: {self.address}\n')

    def compile_source_file(self, file_path):
        with open(file_path, 'r') as f:
            source = f.read()
        compiled_sol = compile_source(source)
        self.contract_id, self.contract_interface = compiled_sol.popitem()



def compile_source_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    return compile_source(source)

#w3 = Web3(EthereumTesterProvider(PyEVMBackend()))
#w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

web3 = iot2blockchian()
contract_source_path = './contracts/storage.sol'
web3.compile_source_file(contract_source_path)
address = web3.deploy_contract()
"""
print(f'Deployed contract to: {address}\n')

store_var_contract = w3.eth.contract(address=address, abi=contract_interface["abi"])

gas_estimate = store_var_contract.functions.setVar(255).estimateGas()
print(f'Gas estimate to transact with setVar: {gas_estimate}')
"""
"""

if gas_estimate < 100000:
    print("Sending transaction to setVar(255)\n")
    tx_hash = store_var_contract.functions.setVar(255).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction receipt mined:")
    pprint.pprint(dict(receipt))
    print("\nWas transaction successful?")
    pprint.pprint(receipt["status"])
else:
     print("Gas cost exceeds 100000")
"""