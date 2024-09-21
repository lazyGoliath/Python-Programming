import UserDefinedLists

def appendi(self,v):   # append, iterative
        if self.isempty():
            self.value = v
            return()
        temp = self
        while temp.next != None:
            temp = temp.next
        newnode = None(v)
        temp.next = newnode
        return()
