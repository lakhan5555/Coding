''' Topological sorting for Directed Acyclic Graph (DAG) is a
   linear ordering of vertices such that for every directed edge u v,
   vertex u comes before v in the ordering. Topological Sorting for
   a graph is not possible if the graph is not a DAG.The first vertex
   in topological sorting is always a vertex with in-degree as 0
   (a vertex with no incoming edges). '''

from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):
        visited = [False]*self.numVertex
        s = []

        for i in range(self.numVertex):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,s)

        print(s[::-1])

    def topologicalSortUtil(self,v,visited,s):
        visited[v] = True

        for x in self.graph[v]:
            if visited[x] == False:
                self.topologicalSortUtil(x,visited,s)
        s.append(v)

if __name__=="__main__":
    G = Graph(6)
    G.add_edge(5,2)
    G.add_edge(5,0)
    G.add_edge(4,0)
    G.add_edge(4,1)
    G.add_edge(2,3)
    G.add_edge(3,1)
    G.topologicalSort()
