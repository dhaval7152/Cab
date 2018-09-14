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

        if not self.matchPrefix(node.address[0], node.mask[0], rule.address[0], rule.mask[0]):
            return False
        if not self.matchPrefix(node.address[1], node.mask[1], rule.address[1], rule.mask[1]):
            return False
        if not self.matchPrefix(node.address[2], node.mask[2], rule.address[2], rule.mask[2]):
            return False
        if not self.matchPrefix(node.address[3], node.mask[3], rule.address[3], rule.mask[3]):
            return False

        return True


    # Find is two pair of (prefix, mask) overlapping
    def matchPrefix(self, addressOne, maskOne, addressTwo, maskTwo):
        maskShort = 0
        if (maskOne > maskTwo):
            maskShort = maskTwo
        else:
            maskShort = maskOne

        return (addressOne & maskShort) == (addressTwo & maskShort)
