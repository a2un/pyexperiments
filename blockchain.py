import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    def new_block(self,proof,previous_hash=None):
        block={
            "index": len(self.chain) + 1,
            "timestamp":time(),
            "transactions":self.current_transactions,
            "proof":proof,
            "previous_hash":previous_hash
        }

        self.current_transactions = []
        self.chain.append(block)
        return block
        
    def new_transaction(self,sender,recipient,amount):
        self.current_transactions.append({
            "sender":sender,
            "reoipient":recepient,
            "amount":amount
        })
        return self.last_block['index'] + 1;

    @staticmethod
    def hash(block):
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    @staticmethod
    def valid_proof(last_proof,proof):
        guess = (str(last_proof) + str(proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4]=="0000"
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof):
            proof+=1

        return proof
    


def main():
    block = {
        "index":1,
        "timestamp":3423423423423.234,
        "transactions":{
            "sender":"kychashS",
            "recipient":"kychashR",
            "amount":"5"
        },
        "proof": 324251234234,
        "previous_hash":'2clhkghf3q42342345odapasuropdhfjkldshfy'
    }