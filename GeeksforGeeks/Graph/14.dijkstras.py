''' Given a graph and a source vertex in the graph, find shortest paths from
  source to all vertices in the given graph
  '''

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = [[0 for col in range(numVertex)]
                      for row in range(numVertex)]

    def printSolution(self,dist):
        print("Vertex \t Distance from Source")
        for node in range(self.numVertex):
            print(node,"\t",dist[node])

    def minDistance(self,dist,sptSet):
        min = float("inf")
        for v in range(self.numVertex):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_inx = v
        return min_inx

    def dijkstra(self,src):
        dist = [float("inf")]*self.numVertex
        sptSet = [False] * self.numVertex
        dist[src] = 0

        for i in range(self.numVertex):
            u = self.minDistance(dist,sptSet)
            sptSet[u] = True

            for v in range(self.numVertex):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > (dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g.dijkstra(0)


'''  The code is for undirected graph, same dijkstra function can be used for
   directed graphs also.

    Dijkstra’s algorithm doesn’t work for graphs with negative weight cycles,
    it may give correct results for a graph with negative edges. For graphs
   with negative weight edges and cycles, Bellman–Ford algorithm can be used,
    we will soon be discussing it as a separate post.
  '''
