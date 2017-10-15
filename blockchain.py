class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    def new_block(self):
        pass
    def new_transaction(self):
        pass

    @staticmethod
    def hash(block):
        pass
    @property
    def last_block(self):
        pass


def main():
    block = {
        "index":1,
        "timestamp":3423423423423.234
        "transactions":{
            "sender":"kychashS",
            "recipient":"kychashR",
            "amount":"5"
        },
        "proof": 324251234234,
        "previous_hash":'2clhkghf3q42342345odapasuropdhfjkldshfy'
    }