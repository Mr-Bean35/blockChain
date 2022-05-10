# File : block.py
# Date : 5/4/2022
# Author : Benjamin Hensley Jr.

import sys, datetime, math, hashlib

class Block():

    def __init__(self, parent_hash, data, timestamp):
        self.parent_hash = parent_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.getHash()

    # Create Genesis Block
    # Static methods do not receive an argument or arguments when they are called
    @staticmethod
    def createGenesisBlock(self):
        return Block("0", "0", datetime.datetime.now())

    def getHash(self):
        self.headerBin = (str(self.parent_hash) +
                     str(self.data) +
                     str(self.timestamp)).encode()

        self.innerHash = hashlib.sha256(self.headerBin).hexdigest().encode()
        self.outerHash = hashlib.sha256(self.innerHash).hexdigest()
        return self.outerHash
