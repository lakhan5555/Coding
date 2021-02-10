from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def connectedComponents(self):
        visited = [False]*self.numVertex
        c = []

        for i in range(self.numVertex):
            if visited[i] == False:
                temp = []
                c.append(self.connectedComponentsUtil(temp,i,visited))
        return c

    def connectedComponentsUtil(self,temp,v,visited):
        visited[v] = True
        temp.append(v)

        for x in self.graph[v]:
            if visited[x] == False:
                temp = self.connectedComponentsUtil(temp,x,visited)

        return temp

if __name__=="__main__":
    G = Graph(5)
    G.add_edge(1,0)
    G.add_edge(2,3)
    G.add_edge(3,4)
    c = G.connectedComponents()
    print("Connected components of undirected Graph")
    for z in c:
        print(z)

''' TC = O(V+E)        
