class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)

    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))