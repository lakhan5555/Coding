from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def detectCylce(self):
        visited = [False]*self.numVertex
        for i in range(self.numVertex):
            if visited[i] == False:
                if self.detectCylceUtil(i,visited,-1):
                    return True
        return False

    def detectCylceUtil(self,v,visited,parent):
        visited[v] = True
        for x in self.graph[v]:
            if visited[x] == False:
                if self.detectCylceUtil(x,visited,v):
                    return True
            elif parent != x:
                return True

        return False

if __name__=="__main__":
    G = Graph(5)
    G.add_edge(1,0)
    G.add_edge(1,2)
    G.add_edge(2,0)
    G.add_edge(0,3)
    G.add_edge(3,4)

    if G.detectCylce():
        print("Graph has cycle")
    else:
        print("Graph has no cycle")

    G1 = Graph(3)
    G.add_edge(0,1)
    G.add_edge(1,2)

    if G1.detectCylce():
        print("Graph has cycle")
    else:
        print("Graph has no cycle")
