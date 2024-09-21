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
        else:  # recursive delete
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None  #set it as last node if recursion is
                                      #complete
        return
    