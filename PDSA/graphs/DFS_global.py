import numpy as np

visited, parent = {}, {}

def neighbours(aMat, v):
    """
    Given an adjacency Matrix aMat and a vertex v;
    returns all neighbours of vertex v
    """
    rows, cols = aMat.shape
    nbrs = []
    for j in range(cols):
        if aMat[v][j] == 1 :
            nbrs.append(j)
    return nbrs

def DFS_init(aMat):
    """
    This function initialises visited and parent dictionaries
    """
    rows, cols = aMat.shape

    for i in range(cols):
        visited[i] = False
        parent[i] = -1
    
    return

def DFS_global(aMat, v):
    """
    Recursive function for Depth first search
    returns visited and parent dictionaries
    """
    visited[v] = True

    for k in neighbours(aMat, v):
        if not visited[k] :
            parent[k] = v
            DFS_global(aMat, k)    
    return

def find_path(aMat, u, v):
    """
    Given an adjaceny matrix aMat and starting and ending vertices u and v resp
    prints path to reach v from u
    """
    DFS_init(A)
    DFS_global(aMat, u)

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
         (1,0), (2,0), (4,0), (2,1), (4,3), (5,3), (6,3), (7,4), (6,5), (7,6), (8,5), (8,7), (9,8)]

A = np.zeros(shape=(10,10))

for (i,j) in edges :
    A[i,j] = 1

print("Path from 0 to 9 : ", find_path(A, 0, 9))
print("Path from 5 to 7 : ", find_path(A, 5, 7))
print("Path from 1 to 6 : ", find_path(A, 1, 6))