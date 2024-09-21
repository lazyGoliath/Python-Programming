import tree

def minval(self):
    if self.left == None:
        return(self.left.value)
    else:
        return(self.left.minval())