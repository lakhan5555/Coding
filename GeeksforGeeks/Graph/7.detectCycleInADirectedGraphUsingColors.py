from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def detectCylce(self):
        color = ["WHITE"]*self.numVertex
        for i in range(self.numVertex):
            if color[i] == "WHITE":
                if self.detectCylceUtil(i,color):
                    return True
        return False

    def detectCylceUtil(self,v,color):
        color[v] = "GREY"

        for x in self.graph[v]:
            if color[x] == "GREY":
                return True
            if color[x] == "WHITE" and self.detectCylceUtil(x,color) == True:
                    return True

        color[v] = "BLACK"
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

if g.detectCylce():
    print("Graph has cycle")
else:
    print("Graph has no cycle")
