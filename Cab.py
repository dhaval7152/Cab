from BucketTree import *

class Cab():
    def __init__(self, ruleName):
        ruleSet = self.getRules(ruleName, thr)
        myTree = BucketTree(ruleSet)

    # ruleSet pharser       ----- to be done
    def getRules(self, ruleName):
        return self

    def query(self, address):
        return(self.myTree.search(address))
