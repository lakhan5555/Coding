from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def detectCylce(self):
        visited = [False]*self.numVertex
        recurStack = [False]*self.numVertex

        for x in range(self.numVertex):
            if visited[x] == False:
                if self.detectCylceUtil(x,visited,recurStack) == True:
                    return True
        return False

    def detectCylceUtil(self,v,visited,recurStack):
        visited[v] = True
        recurStack[v] = True

        for z in self.graph[v]:
            if visited[z] == False:
                if self.detectCylceUtil(z,visited,recurStack) == True:
                    return True
            elif recurStack[z] == True:
                return True

        recurStack[v] = False
        return False

if __name__=="__main__":
    G = Graph(4)
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(1,2)
    G.add_edge(2,0)
    G.add_edge(2,3)
    G.add_edge(3,3)

    if G.detectCylce():
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
