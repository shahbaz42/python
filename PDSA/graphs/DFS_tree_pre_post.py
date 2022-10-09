(visited, pre, post) = ({}, {}, {})

def DFSInitPrePost(aList):
    for i in aList.keys():
        visited[i] = False
        (pre[i], post[i]) = (-1, -1)

def DFSPrePost(aList, v, count):
    visited[v] = True
    pre[v] = count
    count += 1

    for i in aList[v]:
        if not visited[i]:
            count = DFSPrePost(aList, i, count)
    post[v] = count
    count += 1

    return count

def DFSForest(aList, count):
    DFSInitPrePost(aList)
    unvisited = [i for i in aList.keys() if visited[i] == False]
    while(len(unvisited)>0):
        count = DFSPrePost(aList, min(unvisited), count) 
        unvisited = [i for i in aList.keys() if visited[i] == False]   
    return

edges = [ (0,1), (0,4), (2,3), (2,6), (2,7), (3,7), (4,8), (4,9), (6,7), (6,10), (7,10), (7,11), (8,9),
          (1,0), (4,0), (3,2), (6,2), (7,2), (7,3), (8,4), (9,4), (7,6), (10,6), (10,7), (11,7), (9,8)]

A = {}

max_vertex = max([max(i) for i in edges])
min_vertex = min([min(i) for i in edges])

for i in range(min_vertex, max_vertex+1):
    A[i] = []

for (i,j) in edges :
    A[i].append(j)

DFSInitPrePost(A)
DFSForest(A, 0)

print(f"pre".center(5), "|", f"vertex".center(6), "|", f"post".center(5))
for i in A.keys():
    if pre[i] != -1 and post[i] != -1 :
        print(f"{pre[i]}".center(5), "|", f"{i}".center(6), "|", f"{post[i]}".center(5))