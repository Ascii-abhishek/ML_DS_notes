import hashlib
import json
from time import time


class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transaction = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recepient, amount):
        
        self.current_transaction.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):

        block_string = json.dumps(block, sort_keys=True).encode()
        #We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        return hashlib.sha256(block_string).hexdigest()
        

    @property
    def last_block(self):
        return self.chain[-1]

