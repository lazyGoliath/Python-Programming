import tree

def find(self, v):
    if self.isEmpty:
        return(False)
    if self.value == v:  # value found return it
        return(True)
    if v<self.value: # if less than search in the left subtree of BST
        return(self.left.find(v))
    else:
        return(self.right.find(v))