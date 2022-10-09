class Queue:
    """
    Implementattion of Queue using python list
    """
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


def BFS(aList, v):
    """
    Given an adjacency list aList and a vertex v
    performs Depth first search startinmg from vertex v
    returns visited dictionary of all vertices that can be reached starting from v
    returns parent dictionary of recorded path
    """
    (visited, parent) = ({}, {})

    for i in aList.keys():
        visited[i]=False
        parent[i] = -1

    q = Queue()

    visited[v] = True
    q.addQ(v)

    while (not q.isEmpty()):
        c = q.delQ()
        for ngbr_of_c in aList[c]:
            if not visited[ngbr_of_c]:
                visited[ngbr_of_c] = True
                parent[ngbr_of_c] = c
                q.addQ(ngbr_of_c)
    return (visited, parent)


def find_path(aList, u, v):
    """
    Given an adjaceny list aList and starting and ending vertices u and v resp
    prints path to reach v from u
    """
    visited, parent = BFS(aList, u)

    if not visited[v] :
        return "No path Exists"
    
    i = v
    path = []

    while i != -1 :
        path.append(i)
        i = parent[i]
        
    path.reverse()

    return " > ".join([str(x) for x in path])

edges = [(0,1), (0,2), (0,4), (1,2), (3,4), (3,5), (3,6), (4,7), (5,6), (5,7), (5,8), (7,8), (8,9),
         (1,0), (2,0), (4,0), (2,1), (4,3), (5,3), (6,3), (7,4), (6,5), (7,5), (8,5), (8,7), (9,8)]

A = {}

max_vertex = max([max(i) for i in edges])
min_vertex = min([min(i) for i in edges])

for i in range(min_vertex, max_vertex+1):
    A[i] = []

for (i,j) in edges :
    A[i].append(j)

print(A)
print("Path from 0 to 9 : ", find_path(A, 0, 9))
print("Path from 5 to 7 : ", find_path(A, 5, 7))
print("Path from 1 to 6 : ", find_path(A, 1, 6))