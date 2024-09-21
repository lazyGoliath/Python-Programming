from UserDefinedLists import *
import UserDefinedLists

def insert(self,v):
        if self.isempty():
            self.value = v
            return

        newnode = UserDefinedLists.Node(v)

        # Evchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)

        return