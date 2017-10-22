import hashlib
import json
from uuid import uuid4
from textwrap import dedent
from flask import Flask, jsonify, request
import blockchain

app= Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine',methods=['GET']):
def mine():
    return "mined"

@app.route('/transactions/new',methods=['GET'])
def new_transaction():
    values = request.get_json()

    required=['sender','recipient','amount']
    
    return "new txn"

@app.route('/chain',methods=['GET'])
def full_chain():
    response = {
        chain : blockchain.chain,
        length: len(blockchain.chain)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port-5000)
