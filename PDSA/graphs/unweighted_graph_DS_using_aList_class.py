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
    
    def remove_edge(self, start, end):
        """
        
        """
        if (self.has_vertex(start) and self.has_vertex(end)):
            if self.has_edge(start, end):
                self.aList[start].remove(end)
                if not self.directed :
                    self.aList[end].remove(start)
                return True
        return False
    
    def remove_edges(self, edges):
        for(start, end) in edges :
            self.remove_edge(start, end)
        return

    def __DFS_init(self):
        """
        This function initialises visited and parent dictionaries
        """
        self.visited, self.parent = {} , {}

        self.visited = {t:False for t in self.aList.keys()}
        self.parent = {t:-1 for t in self.aList.keys()}

        return
    
    def __DFS_recursive(self, v):
        """
        Recursive function for Depth first search
        returns visited and parent dictionaries
        """
        self.visited[v] = True

        for k in self.aList[v]:
            if not self.visited[k] :
                self.parent[k] = v
                self.__DFS_recursive(k)    
        return
    
    def DFS(self, v):
        """
        This method performs Depth first search and 
        returns visited dict of all vertices that can be reached from vertex v
        returns parent dictionary of recorded path.
        """
        self.__DFS_init()
        self.__DFS_recursive(v)
        return (self.visited, self.parent)
    
    def BFS(self, v):
        """
        This method performs Breadth first search and
        returns visited dict of all vertices that can be reached from vertex v
        returns parent dictionary of recorded path.
        """
        visited = {t:False for t in self.aList.keys()}
        parent = {t:-1 for t in self.aList.keys()}

        q = []

        visited[v] = True 
        q.append(v)

        while(len(q)>0):
            c = q.pop(0)
            for k in self.aList[c]:
                if not visited[k] :
                    visited[k] = True
                    parent[k] = c
                    q.append(k)
        return visited, parent


edges = [ (0,1), (0,4), (2,3), (2,6), (2,7), (3,7), (4,8), (4,9), (6,7), (6,10), (7,10), (7,11), (8,9)]
max_vertex = max([max(i) for i in edges])

g1 = Unweighted_graph(max_vertex + 1, directed=False)
g1.add_edges(edges)
print(g1)
print(g1.BFS(5))
