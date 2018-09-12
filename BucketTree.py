from Bucket import *
from Node import *
from Rule import *

class BucketTree():
    def __init__(self, RuleSet = None):
        self.bucket = Bucket()

        self.dims = self.gen_dim()
        # dim got

        self.splitNode(self.dims)

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

    def splitNode(self, dims):
        for dim in dims:
            cost = self.split(self, dim)

    def split(self, dim):


    def countPrefix(self):
        tmp = self.bucket.node
        sub = 1 << 7
        count = 0
        while tmp > 0:
            tmp -= sub
            sub = sub >> 1
            count += 1
        return count

    def matchRuleAndNode(self, node, rule):

    def matchPrefix(self, addressOne, maskOne, addressTwo):
