# File : blockChain.py
# Date : 5/4/2022
# Author : Benjamin Hensley Jr.

import sys, datetime, math, hashlib
from block import *

b1 = Block.createGenesisBlock('self')
print(b1.hash)

blockChain = [Block.createGenesisBlock('self')]
print(f"The genesis block has been created\n"
      f"Hash: {blockChain[-1].hash}")

# Suppose we want to add blocks to the block chain
numBlocksToAdd = 10
with open('blockChain.txt', 'w') as f:

    for i in range(numBlocksToAdd+1):
        blockChain.append(Block(blockChain[-1].hash, "Data", datetime.datetime.now()))
        print(f"Block #%d has been created" % i)
        print(f"Block #%d hash: %s" % (i, blockChain[i].hash))
        f.write(blockChain[i].hash)
        f.write(f'\n')
