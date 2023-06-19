import numpy as np

class Weighted_graph:
    def __init__(self, vertices, directed=True):
        """
        Initialise the adjacency matrix.
        """
        self.vertices = vertices
        self.directed = directed
        self.aMat = np.zeros((vertices, vertices, 2), dtype=int)
        # self.__DFS_init()
        # self.__BFS_init()
        return
    
    def __str__(self):
        """
        prints the adjacency Matrix.
        """
        return(str(self.aMat))
    
    def has_vertex(self, vertex):
        """
        checks if a vertex is present in the graph.
        """
        return (0 <= vertex < self.vertices)

    def has_edge(self, start, end):
        """
        Checks if an edge is present in the graph.
        """
        if (self.has_vertex(start) and self.has_vertex(end)) :
            if self.aMat[start][end][0] == 1 :
                return True
        return False

    def add_edge(self, start, end, weight):
        """
        adds a weighted edge to the graph.
        """
        if self.has_vertex(start) and self.has_vertex(end):
            if not self.has_edge(start, end):
                self.aMat[start][end] = [1, weight]
                if not self.directed :
                    self.aMat[end][start] = [1, weight]
                return True
        return False
    
    def add_edges(self, edges):
        """
        This method add multiple edges in the graph.
        """
        for (start, end, weight) in edges: 
            self.add_edge(start, end, weight)
    
    def remove_edge(self, start, end):
        """
        This method removes an edge from the graph.
        """
        if (self.has_vertex(start) and self.has_vertex(end)):
            if self.has_edge(start, end):
                self.aMat[start][end] = [0,0]
                if not self.directed :
                    self.aMat[end][start] = [0,0]
                return True
        return False

    

g1 = Weighted_graph(3)
print(f"Empty graph : {g1}")
g1.add_edge(0,1,10)
g1.add_edge(1,2,20)
print(f"After adding two edges {g1}")
g1.remove_edge(0,1)
g1.remove_edge(1,2)
print(f"after removing two edges {g1}")


