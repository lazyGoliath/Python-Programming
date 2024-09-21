from UserDefinedLists import *
import UserDefinedLists

def append(self,v):   # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append(v)
        return