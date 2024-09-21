from tree import *
import tree

def insert(self, v):  #add v as a new leaf
    if self.isEmpty():
        self.value = v
        self.left = Tree() # add 2 empty nodes to the left and right
        self.right = Tree()
    
    if self.value == v: #value foun, do nothing
        return
    
    if self.value < v:
        self.right.insert()
        return
    if self.value > v:
        self.left.insert()
        return
