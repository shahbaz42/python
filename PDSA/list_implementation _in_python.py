class Node:
    def __init__(self, v=None) :
        self.value = v
        self.next = None
    
    def __str__(self):
        if self.isEmpty():
            return "[]"
        temp = self
        output = "["
        while(temp.next != None):
            output += str(temp.value) + ", "
            temp = temp.next
        output += str(temp.value) + "]"
        return output

    def isEmpty(self):
        if self.value == None:
            return True
        else :
            return False
    
    def append(self, v):
        if self.isEmpty():
            self.value = v
        
        elif self.next == None:
            self.next = Node(v)
        
        else :
            self.next.append(v)
    
    def appendi(self, v):
        if self.isEmpty():
            self.value = v
            return
        
        temp = self
        while temp.next != None :
            temp = temp.next

        temp.next = Node(v)
        return

    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return

        newnode = Node(v)
        (newnode.value, self.value) = (self.value, newnode.value)

        newnode.next = self.next
        self.next = newnode

    def delete(self, v):
        """
        delete the first occurance of v in the list.
        """
        # | 4 | 5 | 6 | 3 |
        # if list is empty
        if self.isEmpty():
            return

        # if we have to delete first node
        if self.value == v :
            self.value = None
            if self.next != None :
                self.value = self.next.value
                self.next = self.next.next
            return

        # if we have to delete and middle element
        if self.next != None :
            self.next.delete(v)
            if self.next.value == None:
                self.next = None

ll = Node(1)
ll.append(2)
ll.insert(0)
ll.append(3)
ll.append(4)
ll.appendi(4)
ll.append(5)
ll.delete(4)
ll.append(6)
ll.delete(6)

print(ll)