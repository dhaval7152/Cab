import sys

class Node():

    def __init__(self, parentNode = None, address = [0,0,0,0], mask = [0,0,0,0], thr = 2):
        self.parentNode = parentNode
        self.address = address              # The 4-tuple address of the node [SrcIP, DstIP, SrcPort, DstPort]
        self.mask = mask                    # The 4-tuple masks of the node [same as above]
        self.thr = thr                      # The threshold of one node
        self.dims = []                      # The dimension of cut
        self.relatedRules = []              # The related rules
        self.childNodeList = []             # THe child Nodes of this node
        self.tmpNodeList = []               # The tmp child Nodes of this node

    # got which split is better
    def splitNode(self):

        if len(self.relatedRules) < self.thr:
            return

        # get dim for split
        self.dims = self.gen_dim()

        cost = sys.maxint
        bestDim = []
        for dim in self.dims:
            tmpCost = self.split(dim)

            # if best cut
            if tmpCost < cost:
                bestDim = list(dim)
                self.childNodeList = list(self.tmpNodeList)
                cost = tmpCost

            self.tmpNodeList = []

        for childNode in self.childNodeList:
            if len(childNode.relatedRules) > self.thr:
                childNode.splitNode()

        # print cost

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

        tmpList = []
        # cal the tmp split
        for i in range(4):

            if i <= 1:
                totalDigits = 32
            else:
                totalDigits = 16
            # this dimension needs one cut
            if dim[i] == 1:
                digits = bin(self.mask[i]).count("1")
                if (digits > totalDigits - 1):
                    return sys.maxint

                # Add left child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (1 << (totalDigits - 1 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (0 << (totalDigits - 1 - digits))
                tmpList.append(tmpChild)

                # Add right child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (1 << (totalDigits - 1 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (1 << (totalDigits - 1 - digits))
                tmpList.append(tmpChild)

            # this dimension needs two cut
            if dim[i] == 2:
                digits = bin(self.mask[i]).count("1")
                if (digits > totalDigits - 2):
                    return sys.maxint

                # Add first child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (3 << (totalDigits - 2 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (0 << (totalDigits - 2 - digits))
                tmpList.append(tmpChild)

                # Add second child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (3 << (totalDigits - 2 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (1 << (totalDigits - 2 - digits))
                tmpList.append(tmpChild)

                # Add third child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (3 << (totalDigits - 2 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (2 << (totalDigits - 2 - digits))
                tmpList.append(tmpChild)

                # Add fourth child
                tmpChild = Node(self, list(self.address), list(self.mask))
                tmpChild.mask[i] = tmpChild.mask[i] + (3 << (totalDigits - 2 - digits))
                tmpChild.address[i] = tmpChild.address[i] + (3 << (totalDigits - 2 - digits))
                tmpList.append(tmpChild)

        # Add rules for each childNode
        for childNode in tmpList:
            for rule in self.relatedRules:
                if self.matchRuleAndNode(childNode, rule):
                    childNode.relatedRules.append(rule)

        self.tmpNodeList[:] = [childNode for childNode in tmpList if len(childNode.relatedRules) > 0]

        sum = 0

        for childNode in self.tmpNodeList:
            sum += len(childNode.relatedRules)

        return sum

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

