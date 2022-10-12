class Unweighted_graph:
    def __init__(self, vertices, directed=True):
        """
        initialise the adjacency list
        """
        self.vertices = vertices
        self.directed = directed
        self.aList = {t:[] for t in range(vertices)}
    
    def __str__(self):
        """
        prints adjacency list
        """
        return(str(self.aList))
    
    def has_vertex(self, vertex):
        """
        This method checks if a vertex is present in hgraph or not.
        """
        return (0 <= vertex < self.vertices)
    
    def has_edge(self, start, end):
        """
        This method checks if an edge is present in graph or not.
        """
        if (self.has_vertex(start) and self.has_vertex(end)):
            if end in self.aList[start] :
                return True
        return False
    
    def add_edge(self, start, end):
        """
        This method add an edge to the graph.
        """
        if (self.has_vertex(start) and self.has_vertex(end)):
            if not self.has_edge(start, end):
                self.aList[start].append(end)
                if not self.directed:
                    self.aList[end].append(start)
                return True
        return False
    
    def add_edges(self, edges):
        """
        This method adds multiple edges to the graph
        """
        for (start, end) in edges:
            self.add_edge(start, end)
        return 

    def toposort(self):
        (indegree, toposort_seq) = ({t:0 for t in  range(self.vertices)}, [])
        
        for i in self.aList:
            for j in self.aList[i]:
                indegree[j] += 1
        
        q = [i for i in range(self.vertices) if indegree[i] == 0]

        while(len(q)> 0):
            c = q.pop(0)
            toposort_seq.append(c)
            indegree[c] -= 1
            for k in self.aList[c] :
                indegree[k] -= 1
            q = [i for i in range(self.vertices) if indegree[i] == 0 ]

        return(toposort_seq)

edges = [(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(3,5),(3,7),(4,7),(5,6),(6,7)]
g1 = Unweighted_graph(8, directed=True)
g1.add_edges(edges)
print(g1.aList)

print(g1.toposort())
    


