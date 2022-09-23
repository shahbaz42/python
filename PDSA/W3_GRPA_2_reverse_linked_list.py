from audioop import reverse
from logging import root


class Node:
    def __init__(self, v=None):
        self.value = v
        self.next =None

    def __str__(self):
        if self.isEmpty():
            return ""
        temp = self
        output = "["
        while temp.next != None:
            output += str(temp.value) + ","
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
        elif self.next==None:
            self.next = Node(v)
        else:
            self.next.append(v)

    def appendi(self, v):
        if self.isEmpty():
            self.value = v
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v)
        return            

    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return
        
        newnode = Node(v)
        (self.value, newnode.value) =(newnode.value, self.value)
        self.next, newnode.next = newnode, self.next
    
    def delete(self, v):
        # 1 2 3 4 5
        # list is empty
        if self.isEmpty():
            return
        # delte the first node
        if self.value == v:
            self.value=None # first node only
            if self.next != None:
                self.value, self.next.value = self.next.value, self.next
                self.next = self.next.next
            return
        # delete any other node
        else:
            if self.next != v:
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

def reverse(root):
        prev = None
        current = root
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

ll = Node(1)
ll.append(2)
ll.append(3)
print(ll)
ll = reverse(ll)
print(ll)
ll.reverse()
print(ll)