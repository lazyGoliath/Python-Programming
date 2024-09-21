import tree

def inorder(self):
    # if empty return empty list
    if self.isEmpty:
        return([])
    else:
        #left subtree()+root+right subtree()
        return(self.left.inorder()+[self.value]+self.roght.inorder())
    
def __str__(self):
    return(str(self.inorder()))