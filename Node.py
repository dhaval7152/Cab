class Node():

    def __init__(self, parentNode = None, address = [0,0,0,0], mask = [0,0,0,0]):
        self.parentNode = parentNode;
        self.address = address;
        self.mask = mask;

    address = []        # The 4-tuple address of the node [SrcIP, DstIP, SrcPort, DstPort]
    mask = []           # The 4-tuple masks of the node [same as above]

    relatedRules = []   # The related rules

    parentNode = None   # The parent Node of this node
    childNodeList = []  # THe child Nodes of this node
