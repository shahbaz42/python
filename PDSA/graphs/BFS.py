import numpy as np

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

def neighbours(aMat, v):
    rows, cols = aMat.shape
    nbrs = []
    for j in range(cols):
        if aMat[v][j] == 1 :
            nbrs.append(j)
    return nbrs

def BFS(aMat, v):
    visited = {}
    rows, cols = aMat.shape

    for i in range(rows):
        visited[i]=False

    q = Queue()

    visited[v] = True
    q.addQ(v)

    while (not q.isEmpty()):
        c = q.delQ()
        for ngbr_of_c in neighbours(aMat, c):
            if not visited[ngbr_of_c]:
                visited[ngbr_of_c] = True
                q.addQ(ngbr_of_c)

    return visited

edges = [(0,1), (0,2), (0,4), (1,2), (3,4), (3,5), (3,6), (4,7), (5,6), (5,7), (5,8), (7,8), (8,9),
         (1,0), (2,0), (4,0), (2,1), (4,3), (5,3), (6,3), (7,4), (6,5), (7,6), (8,5), (8,7), (9,8)]

A = np.zeros(shape=(10,10))

for (i,j) in edges :
    A[i,j] = 1

print(BFS(A, 0))