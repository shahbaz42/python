class graph:
    def __init__(self, vertices, edges):
        self.aList = { t:[] for t in vertices} 
        self.vertices = vertices

        for (u,v) in edges :
            self.aList[u].append(v)

    def __str__(self):
        return(str(self.aList))
    
    def BFS(self, v):
        visited = {t:False for t in self.vertices}
        
        visited[v] = True
        q = [v]

        while(len(q)>0):
            t = q.pop(0)
            for k in self.aList[t]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
        return visited

    def findMasterTank(self):
        indegree = {t:0 for t in self.vertices}

        # calculating indegree of each vertices        
        for (u,v) in self.aList.items():
            for k in v :
                indegree[k] += 1
        
        # a is a list of all vertices with indegree == 0
        a = [i for (i,j) in indegree.items() if j == 0]
        
        # we need to run bfs from verteces in a to see if every other vertex is reachable.
        for i in a :
            isMaster = True
            # run BFS to see if every other vertex is reachable from i
            result = self.BFS(i)
            for value in result.values():
                if not value:
                    isMaster = False
                    break
            if isMaster:
                return i
        return 0
        
# taking input
vertices = [int(i) for i in input().split()]
E = int(input())
edges = []
for i in range(E):
    (u,v)=[int(i) for i in input().split()]
    edges.append((u,v))

g1 = graph(vertices, edges)
print(g1.findMasterTank())