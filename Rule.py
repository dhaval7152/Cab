class Rule():

    def __init__(self, priority = 0, address = [0,0,0,0], mask = [0,0,0,0]):
        self.priority = priority
        self.address = address
        self.mask = mask

    address = []        # The 4-tuple address of the node [SrcIP, DstIP, SrcPort, DstPort]
    mask = []           # The 4-tuple masks of the node [same as above]
    priority = 0        # The priority of the rule, dafault as 0