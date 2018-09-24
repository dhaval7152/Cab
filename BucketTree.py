from Bucket import *
from Node import *
from Rule import *
import socket
import struct

class BucketTree():
    def __init__(self, fileName = None, thr = 5):
        self.root = Node(thr = thr)

        # parse the ruleFile and load all rules into root's relatedRules
        self.loadRootRules(fileName)

        # start to split the root of BucketTree
        self.root.splitNode()

    root = Node()       # The root node of bucketTree
    thr = 0             # The threshold of one bucket

    # load ruleSet into the root of bucketTree
    def loadRootRules(self, fileName):

        ruleFile = open(fileName, 'r')

        for line in ruleFile:

            # some prepare job
            line = line.replace('@', ' ')
            line = line.replace(':', ' ')
            line = line.replace('/', ' ')

            rule = line.split()

            # get source IP
            srcIPAddr = self.ip2int(rule[0])
            srcIPMask = self.generateMask(int(rule[1]), 32)
            dstIPAddr = self.ip2int(rule[2])
            dstIPMask = self.generateMask(int(rule[3]), 32)
            if rule[4] == rule[5]:
                srcPortAddr = int(rule[4])
                srcPortMask = self.generateMask(16, 16)
            else:
                srcPortAddr = 0
                srcPortMask = self.generateMask(0, 16)
            if rule[6] == rule[7]:
                dstPortAddr = int(rule[6])
                dstPortMask = self.generateMask(16, 16)
            else:
                dstPortAddr = 0
                dstPortMask = self.generateMask(0, 16)
            addr = [srcIPAddr, dstIPAddr, srcPortAddr, dstPortAddr]
            mask = [srcIPMask, dstIPMask, srcPortMask, dstPortMask]
            tmpRule = Rule(0, addr, mask)

            self.root.relatedRules.append(tmpRule)

    def ip2int(self,addr):
        return struct.unpack("!I", socket.inet_aton(addr))[0]

    def generateMask(self, digits, total):
        sum = 0
        for i in range(total - digits, total):
            sum += 1 << i
        return sum