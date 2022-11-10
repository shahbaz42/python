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
    
    def dijkstra(self, s): 
        """
        This method performs diskstra algroithm from starting vertex s and 
        returns distance dict.
        """
        # initializing rows, columns, x distance and visited dict
        (rows, cols, x) = self.aMat.shape
        infinity = np.max(self.aMat)*rows + 1
        (visited, distance) = ({t:False for t in range(rows)}, {t:infinity for t in range(rows)})

        distance[s] = 0

        for u in range(rows):
            # finding the mining distance from all vertices which has not been visited
            nextd = min([distance[v] for v in range(rows) if not visited[v]])
            # there may be many such vertices v which have minimum distance = nextd so we may need to make an array
            nextvList = [v for v in range(rows) if not visited[v] and distance[v] == nextd]

            # if list to visit next is empty
            if nextvList == [] :
                break

            nextv = min(nextvList)
            visited[nextv] = True

            for v in range(rows) :
                if not visited[v] and self.aMat[nextv, v, 0] == 1 :
                    distance[v] = min(distance[v], distance[nextv]+self.aMat[nextv, v, 1])

        return distance


g1 = Weighted_graph(3)

g1.add_edge(0,1,10)
g1.add_edge(1,2,20)

print(g1.dijkstra(0))