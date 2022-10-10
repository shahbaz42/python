visited, parent = {}, {}

def DFSInit(aList):
    for i in aList.keys():
        visited[i] = False
        parent[i] = -1
    return

def DFS(aList, v):
    visited[v] = True
    for k in aList[v]:
        if not visited[k] :
            DFS(aList, k)
            parent[k] = v
    return

def components(aList):
    """
    Given an adjacency list aList
    this function returns a component dictionary using DFS.
    """
    components, compid = ({}, 0)
    for i in aList.keys():
        components[i] = -1

    min_vertex = min(aList.keys())
    unexplored = [i for i in components.keys() if components[i] == -1]
    DFSInit(aList)
    while(len(unexplored)>0):
        DFS(aList, min(unexplored))
        for i in unexplored :
            if visited[i] :
                components[i] = compid
        compid += 1
        unexplored = [i for i in unexplored if components[i] == -1]        

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

print(components(A))