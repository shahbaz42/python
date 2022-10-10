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
        return (0 <= vertex < self.vertices)
    
    def has_edge(self, start, end):
        if (self.has_vertex(start) and self.has_vertex(end)):
            if end in self.aList[start] :
                return True
        return False
    
    def add_edge(self, start, end):
        if (self.has_vertex(start) and self.has_vertex(end)):
            if not self.has_edge(start, end):
                self.aList[start].append(end)
                if not self.directed:
                    self.aList[end].append(start)
                return True
        return False
    
    def add_edges(self, edges):
        for (start, end) in edges:
            self.add_edge(start, end)
        return 
    
    def remove_edge(self, start, end):
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

        for i in self.aList.keys():
            self.visited[i] = False
            self.parent[i] = -1
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
        self.__DFS_init()
        self.__DFS_recursive(v)
        return (self.visited, self.parent)

edges = [ (0,1), (0,4), (2,3), (2,6), (2,7), (3,7), (4,8), (4,9), (6,7), (6,10), (7,10), (7,11), (8,9)]
max_vertex = max([max(i) for i in edges])

g1 = Unweighted_graph(max_vertex + 1, directed=False)
g1.add_edges(edges)
print(g1)
