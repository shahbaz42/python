class Queue:
    def __init__(self):
        self.Q = []
    
    def __str__(self):
        return(str(self.Q))

    def isEmpty(self):
        return len(self.Q) == 0
    
    def size(self):
        return len(self.Q)

    def addQ(self, x):
        self.Q.append(x)
    
    def delQ(self):
        if not self.isEmpty():
            v = self.Q[0]
            self.Q = self.Q[1:]
            return v
        raise Exception("Can't remove Queue is empty.")

q1 = Queue()
print(q1)

for i in range(4):
    q1.addQ(i)
    print(q1)

print(q1.isEmpty())
print(q1.size())

for i in range(4):
    q1.delQ()
    print(q1)

print(q1)
print(q1.isEmpty())