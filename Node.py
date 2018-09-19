class Node():

    def __init__(self, parentNode = None, address = [0,0,0,0], mask = [0,0,0,0]):
        self.parentNode = parentNode
        self.address = address
        self.mask = mask

    address = []        # The 4-tuple address of the node [SrcIP, DstIP, SrcPort, DstPort]
    mask = []           # The 4-tuple masks of the node [same as above]

    relatedRules = []   # The related rules

    parentNode = None   # The parent Node of this node
    childNodeList = []  # THe child Nodes of this node
    chileNum = 0        # The num of child Nodes of this node

    # got which split is better
    def splitNode(self, dims, thr):
        cost = sys.maxint
        bestDim = []
        for dim in dims:
            tmpCost = self.split(dim, thr)

            if tmpCost < cost:
                bestDim = dim

            self.childNodeList = []
            self.chileNum = 0

    def split(self, dim, thr):
        digits = 0;

        # got the tmp split
        for i in range(4):

            # this dimension needs one cut
            if dim[i] == 1:
                digits = self.countOnes(self.mask[i])

                tmpChild = Node()
                tmpChild.mask = self.mask
                tmpChild.node.address = self.address

                # Add left child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 1 << (31 - digits)
                tmpChild.address[i] = self.address[i] + 0 << (31 - digits)
                self.childNodeList.append(tmpChild)

                # Add right child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 1 << (31 - digits)
                tmpChild.address[i] = self.address[i] + 1 << (31 - digits)
                self.childNodeList.append(tmpChild)

            # this dimension needs two cut
            if dim[i] == 2:
                digits = self.countOnes(self.mask[i])

                tmpChild = Node()
                tmpChild.mask = self.mask
                tmpChild.address = self.address

                # Add first child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 3 << (30 - digits)
                tmpChild.address[i] = self.address[i] + 0 << (30 - digits)
                self.childNodeList.append(tmpChild)

                # Add second child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 3 << (30 - digits)
                tmpChild.address[i] = self.address[i] + 1 << (30 - digits)
                self.childNodeList.append(tmpChild)

                # Add third child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 3 << (30 - digits)
                tmpChild.address[i] = self.address[i] + 2 << (30 - digits)
                self.childNodeList.append(tmpChild)

                # Add fourth child
                self.childNum += 1
                tmpChild.mask[i] = self.address[i] + 3 << (30 - digits)
                tmpChild.address[i] = self.address[i] + 3 << (30 - digits)
                self.childNodeList.append(tmpChild)

        # Add rules for each childNode
        for childNode in self.childNodeList:
            for rule in self.relatedRules:
                if self.matchRuleAndNode(childNode, rule):
                    childNode.relatedRules.append(rule)

        for childNode in self.childNodeList:
            if len(childNode.relatedRules) > thr:
                childNode.split(dim, thr)

        sum = 0
        for childNode in self.childNodeList:
            sum += len(childNode.relatedRules)

        return sum


    def countOnes(self, tmp):
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

