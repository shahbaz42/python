import numpy as np

def DFS_init(aList):
    """
    This function initialises visited and parent dictionaries
    """
    visited, parent = {}, {}

    for i in aList.keys():
        visited[i] = False
        parent[i] = -1
    
    return visited, parent

def DFS(aList, visited, parent, v):
    """
    Recursive function for Depth first search
    returns visited and parent dictionaries
    """
    visited[v] = True

    for k in aList[v]:
        if not visited[k] :
            parent[k] = v
            visited, parent = DFS(aList, visited, parent, k)    
    return visited, parent

def find_path(aList, u, v):
    """
    Given an adjaceny matrix aMat and starting and ending vertices u and v resp
    prints path to reach v from u
    """
    visited, parent = DFS_init(A)
    visited, parent = DFS(aList, visited, parent, u)

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

print(max_vertex, min_vertex)

for i in range(min_vertex, max_vertex+1):
    A[i] = []

for (i,j) in edges :
    A[i].append(j)

print(A)
print("Path from 0 to 9 : ", find_path(A, 0, 9))
print("Path from 5 to 7 : ", find_path(A, 5, 7))
print("Path from 1 to 6 : ", find_path(A, 1, 6))