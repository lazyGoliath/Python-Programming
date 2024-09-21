class Tree:
    def __init__(self, initval=None): #none value by default
        self.value = initval
        if self.value: #if there is value other than none
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return
    
    def isEmpty(self):
        return self.value == None