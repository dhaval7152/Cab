from Bucket import *
from Node import *
from Rule import *

class BucketTree():
    def __init__(self, RuleSet = None):
        self.bucket = Bucket()
        self.childNum = 0
        self.children = []

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

    # got which split is better
    def splitNode(self, dims):
        for dim in dims:
            cost = self.split(dim)
            return cost

    def split(self, dim):
        digits = 0
        for i in range(4):

            # this dimension needs one cut
            if dim[i] == 1:
                digits = self.countOnes(self.bucket.node.mask[i])

                self.oneDimOneCut();

                
            # this dimension needs two cut
            if dim[i] == 2:
                digits = self.countOnes(self.bucket.node.mask[i])






        return digits

    def oneDimOneCut(self):
        tmpChild = Bucket()
        tmpChild.node.mask = self.bucket.node.mask
        tmpChild.node.address = self.bucket.node.address

        # Add left child
        self.childNum += 1
        tmpChild.node.mask[i] = self.bucket.node.address[i] + 1 << (8 - digits)
        tmpChild.node.address[i] = self.bucket.node.address[i]
        self.children.append(tmpChild)

        # Add right child
        self.childNum += 1
        tmpChild.node.mask[i] = self.bucket.node.address[i] + 1 << (8 - digits)
        tmpChild.node.address[i] = self.bucket.node.address[i] + 1 << (8 - digits)
        self.children.append(tmpChild)

    def oneDimTwoCut(self):


    def countOnes(self, tmp):
        sub = 1 << 7
        count = 0
        while tmp > 0:
            tmp -= sub
            sub = sub >> 1
            count += 1
        return count

    # This function is to judge whether the node is associated with the rule
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
