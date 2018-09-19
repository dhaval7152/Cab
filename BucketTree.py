from Bucket import *
from Node import *
from Rule import *

class BucketTree():
    def __init__(self, ruleName = None, thr = 5):
        self.root = Node()

        self.dims = self.gen_dim()
        # dim got

        ruleSet = self.ruleSetParser(ruleName)

        self.loadRootRules(ruleSet)

        self.root.splitNode(dims, thr)

        self.thr = thr

    root = Node()       # The root node of bucketTree
    dims = []           # The dimension of cut
    thr = 0             # The threshold of one bucket

    # cal the dim of split
    def gen_dim(self):
        dims = []
        init = [0, 0, 0, 0]
        for x in range(4):
            for y in range(4):
                init[x] += 1
                init[y] += 1
                dims.append(init)
                init = [0, 0, 0, 0]
        return dims

    # load ruleSet into the root of bucketTree
    def loadRootRules(self, ruleSet):
        for rule in ruleSet:
            self.root.append(rule)

    # get a string of fileName, return a list of rules
    def ruleSetParser(self, ruleName):
        return ruleSet