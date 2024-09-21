from maxVal import maxval
import tree
import maxVal

def delete(self, v):
    if self.isEmpty():
        return
    
    if v < self.value:
        self.left(v)
        return
    elif v > self.value:
        self.right(v)
        return
    else:
        if self.isLeaf():
            self.makeEmpty()
        elif self.left.isEmpty():
            self.copyRight()
        else:
            self.value = self.left.maxval()
            self.left.delete(self.left.maxval())
            return
        
#convert leaf to empty node
def makeEmpty(self):
    self.value = None
    self.left = None
    self.right = None
    return

# copy right child values to current node
def copyRight(self):
    self.value = self.right.value
    self.left = self.right.left
    self.right = self.right.right
    return
