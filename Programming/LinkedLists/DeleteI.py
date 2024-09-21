import UserDefinedLists

def delete(self,v):   # delete
        if self.isempty():
            return

        if self.value == v:  #value to delete is in 1st node
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return