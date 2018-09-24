import sys

class Node():

    def __init__(self, parentNode = None, address = [0,0,0,0], mask = [0,0,0,0], thr = 5):
        self.parentNode = parentNode
        self.address = address
        self.mask = mask
        self.thr = thr

    address = []        # The 4-tuple address of the node [SrcIP, DstIP, SrcPort, DstPort]
    mask = []           # The 4-tuple masks of the node [same as above]

    dims = []           # The dimension of cut
    relatedRules = []   # The related rules

    parentNode = None   # The parent Node of this node
    childNodeList = []  # THe child Nodes of this node
    tmpNodeList = []    # The tmp child Nodes of this node

    # got which split is better
    def splitNode(self):
        # get dim for split
        self.dims = self.gen_dim()
        print "dim got"

        cost = sys.maxint
        bestDim = []
        for dim in self.dims:
            tmpCost = self.split(dim)
            print tmpCost

            # if best cut
            if tmpCost < cost:
                bestDim = list(dim)
                self.childNodeList = list(self.tmpNodeList)

            self.tmpNodeList = []
            print len(self.tmpNodeList)

        return cost

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

    def split(self, dim):

        # cal the tmp split
        for i in range(4):

            if i <= 1:
                totalDigits = 32
            else:
                totalDigits = 16
            # this dimension needs one cut
            if dim[i] == 1:
                digits = self.countOnes(self.mask[i], totalDigits)

                tmpChild = Node()
                tmpChild.address = list(self.address)
                tmpChild.mask =  list(self.mask)

                # Add left child
                tmpChild.mask[i] = self.address[i] + 1 << (totalDigits - 1 - digits)
                tmpChild.address[i] = self.address[i] + 0 << (totalDigits - 1 - digits)
                self.tmpNodeList.append(tmpChild)

                # Add right child
                tmpChild.mask[i] = self.address[i] + 1 << (totalDigits - 1 - digits)
                tmpChild.address[i] = self.address[i] + 1 << (totalDigits - 1 - digits)
                self.tmpNodeList.append(tmpChild)

            # this dimension needs two cut
            if dim[i] == 2:
                digits = self.countOnes(self.mask[i], totalDigits)

                tmpChild = Node()
                tmpChild.address = list(self.address)
                tmpChild.mask = list(self.mask)

                # Add first child
                tmpChild.mask[i] = self.address[i] + 3 << (totalDigits - 2 - digits)
                tmpChild.address[i] = self.address[i] + 0 << (totalDigits - 2 - digits)
                self.tmpNodeList.append(tmpChild)

                # Add second child
                tmpChild.mask[i] = self.address[i] + 3 << (totalDigits - 2 - digits)
                tmpChild.address[i] = self.address[i] + 1 << (totalDigits - 2 - digits)
                self.tmpNodeList.append(tmpChild)

                # Add third child
                tmpChild.mask[i] = self.address[i] + 3 << (totalDigits - 2 - digits)
                tmpChild.address[i] = self.address[i] + 2 << (totalDigits - 2 - digits)
                self.tmpNodeList.append(tmpChild)

                # Add fourth child
                tmpChild.mask[i] = self.address[i] + 3 << (totalDigits - 2 - digits)
                tmpChild.address[i] = self.address[i] + 3 << (totalDigits - 2 - digits)
                self.tmpNodeList.append(tmpChild)

        print len(self.tmpNodeList), len(self.relatedRules)
        for childNode in self.tmpNodeList:
            for rule in childNode.relatedRules:
                print rule.address
        # Add rules for each childNode
        for childNode in self.tmpNodeList:
            for rule in self.relatedRules:
                if self.matchRuleAndNode(childNode, rule):
                    childNode.relatedRules.append(rule)



        for childNode in self.tmpNodeList:
            if len(childNode.relatedRules) > self.thr:
                childNode.splitNode()

        sum = 0
        for childNode in self.tmpNodeList:
            sum += len(childNode.relatedRules)

        return sum


    def countOnes(self, tmp, totaldigits):
        # print tmp, totaldigits
        sub = 1 << (totaldigits - 1)
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

