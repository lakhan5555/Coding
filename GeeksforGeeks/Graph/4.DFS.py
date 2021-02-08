from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=" ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i,visited)

    def DFS(self,v):
        visited = set()
        self.DFSUtil(v,visited)

if __name__=="__main__":
    G = Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(1,2)
    G.add_edge(2,0)
    G.add_edge(2,3)
    G.add_edge(3,3)

    print("DFS of graph from vertex 2: ")
    G.DFS(2)

''' TC = O(V + E)
    SC = O(V)
    '''

''' for disconnected graph '''
'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=" ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i,visited)

    def DFS(self):
        visited = set()
        for x in list(self.graph):
            if x not in visited:
                self.DFSUtil(x,visited)

if __name__=="__main__":
    G = Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(1,2)
    G.add_edge(2,0)
    G.add_edge(2,3)
    G.add_edge(3,3)

    G.DFS()  '''

''' TC = O(V + E)
    SC = O(V) '''
