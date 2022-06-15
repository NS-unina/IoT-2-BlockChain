from flask import Flask
from bcmanager import *

app = Flask(__name__)

contract = iot2blockchian()
contract.address = "0xD3f38326f2665809b2A0BaB863aD2520cC029374"

@app.route("/")
def hello_world():
    global contract
    #contract.address = "0xD3f38326f2665809b2A0BaB863aD2520cC029374"
    return contract.address


@app.route('/contract/<string:add_contract>')
def show_post(add_contract):
    global contract
    contract.address = add_contract
    return contract.address
