class LinkedList:
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
            self.next = LinkedList(v)
        
        else :
            self.next.append(v)
    
    def appendi(self, v):
        if self.isEmpty():
            self.value = v
            return
        
        temp = self
        while temp.next != None :
            temp = temp.next

        temp.next = LinkedList(v)
        return

    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return

        newnode = LinkedList(v)
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
    
    def reverse(self):
        if self.next == None : #if linked list is having single node
            return
        elif self.next.next == None : # if linked list is having two nodes
            (self.next.value, self.value) = (self.value, self.next.value)
            return

        (prev, current, next, second) = (None, self, self.next, self.next)

        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        """
        before plumbing : 

        self                    prev ; next, current = None
        |                       |
        1 <-- 2 <-- 3 <-- 4 <-- 5
              |
              second

        after plumbing :

        self    ---2---->---------
         |      |                |
        (5)     2 <-- 3 <-- 4   (1)---> None 
         |                  |      
         ------1-->----------

        """

        (self.value, prev.value) = (prev.value, self.value) # swapping self with last node
        self.next = prev.next #1
        second.next = prev #2
        prev.next = None
        
        return

ll = LinkedList()
print("Empty linked list :", ll)

ll.reverse()
print("Reverse of empty linked list :", ll)

ll.append(0)
print("append 0 :", ll)

ll.reverse()
print("reverse :", ll)

ll.append(1)
print("append 1 :", ll)

ll.reverse()
print("reverse :", ll)

ll.insert(2)
print("insert 2 :", ll)

ll.reverse()
print("reverse :", ll)

ll.delete(1)
print("delete 1 :", ll)