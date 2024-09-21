import tree

def maxval(self):
    if self.right == None:
        return(self.right.value)
    else:
        return(self.right.maxval())