import json
import logging
import random
import sys
import time
from datetime import datetime
from typing import Iterator
from bcmanager import iot2blockchian
from flask import Flask, Response, render_template, request, stream_with_context

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

application = Flask(__name__)
random.seed()  # Initialize the random number generator

testFlag = False
contract = iot2blockchian()
id_event = ""
block_filter = ""
 
@application.route("/")
def index() -> str:
    return render_template("index.html")

def handle_event(event):
    receipt = contract.w3.eth.waitForTransactionReceipt(event['transactionHash'])
    result = id_event.processReceipt(receipt) # Modification
    #logger.info(result[0]['args']["_var"])
    return result[0]['args']["iotData"]
    #print(result[0]['args']["_var"])
    #print(type(result[0]['args']))

def generate_random_data() -> Iterator[str]:
    data1 = 0
    data2 = 0
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr or ""

    try:
        logger.info("Client %s connected", client_ip)
        if testFlag == True:
            while True:
                for event in block_filter.get_new_entries():
                    data = handle_event(event)
                    if(data[0]=="data1"):
                        data1 = data[1]
                    else: 
                        data2 = data[1]
                    json_data = json.dumps(
                        {
                            "value": data1,
                            "value2": data2,
                            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    )
                    yield f"data:{json_data}\n\n"
                    time.sleep(1)
    except GeneratorExit:
        logger.info("Client %s disconnected", client_ip)

@application.route("/chart-data")
def chart_data() -> Response:
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/contract/<string:add_contract>')
def show_post(add_contract):
    global contract
    global testFlag
    global id_event
    global block_filter

    contract.address = add_contract
    testFlag = True
    
    f = open("abi.txt", "r")
    abi2 = f.read()

    id_contract = contract.w3.eth.contract(address=contract.address, abi=abi2)
    id_event = id_contract.events.valueRequest()
    block_filter = contract.w3.eth.filter({'fromBlock':'latest', 'address':contract.address})

    
    return contract.address



if __name__ == "__main__":
    testFlag = False
    application.run(host="0.0.0.0", threaded=True)