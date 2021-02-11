''' A directed graph is strongly connected if there is a path between all
pairs of vertices. A strongly connected component (SCC) of a directed graph
 is a maximal strongly connected subgraph.
'''

from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,i,visited):
        visited[i] = True
        print(i,end=" ")

        for v in self.graph[i]:
            if visited[v] == False:
                self.DFSUtil(v,visited)

    def fillOrder(self,v,visited,stack):
        visited[v] = True

        for u in self.graph[v]:
            if visited[u] == False:
                self.fillOrder(u,visited,stack)
        stack = stack.append(v)

    def transpose(self):
        g = Graph(self.numVertex)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j,i)
        return g

    def SCC(self):
        visited = [False] * self.numVertex

        stack = []

        for x in range(self.numVertex):
            if visited[x] == False:
                self.fillOrder(x,visited,stack)

        gr = self.transpose()
        visited = [False]*self.numVertex

        while stack:
            v = stack.pop()
            if visited[v] == False:
                gr.DFSUtil(v,visited)
                print()

if __name__ == "__main__":
    G = Graph(5)
    G.add_edge(1,0)
    G.add_edge(0,2)
    G.add_edge(2,1)
    G.add_edge(0,3)
    G.add_edge(3,4)

    print("Strongly connected components are:")
    G.SCC()


''' TC = O(V+E) '''
