class Node:
    def __init__(self, v=None) :
        self.value = v
        self.next = None

    def is_empty(self):
        if self.value == None:
            return True
        else :
            return False

    
l1 = Node(5)
l2 = Node()

print(l1.is_empty())
print(l2.is_empty())