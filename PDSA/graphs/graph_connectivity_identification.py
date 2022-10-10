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

def components(aList):
    """
    Given an adjacency list aList
    this function returns a component dictionary using BFS.
    """

    (components, compid) = ({}, 0)
    for i in aList.keys():
        components[i] = -1

    unvisited = [i for i in aList.keys() if components[i] == -1]
    while(len(unvisited)>0):
        visited, parent = BFS(aList, min(unvisited))
        for i in unvisited:
            if visited[i]:
                components[i] = compid
        compid += 1
        unvisited = [i for i in aList.keys() if components[i] == -1]

    return components

edges = [ (0,1), (0,4), (2,3), (2,6), (2,7), (3,7), (4,8), (4,9), (6,7), (6,10), (7,10), (7,11), (8,9),
          (1,0), (4,0), (3,2), (6,2), (7,2), (7,3), (8,4), (9,4), (7,6), (10,6), (10,7), (11,7), (9,8)]

A = {}

max_vertex = max([max(i) for i in edges])
min_vertex = min([min(i) for i in edges])

for i in range(min_vertex, max_vertex+1):
    A[i] = []

for (i,j) in edges :
    A[i].append(j)

cmp =  components(A)
print(cmp)