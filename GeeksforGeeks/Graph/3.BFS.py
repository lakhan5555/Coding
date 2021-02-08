from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*(max(self.graph)+1)

        q = []
        q.append(s)
        visited[s] = True

        while len(q):
            temp = q.pop(0)
            print(temp,end=" ")

            for i in self.graph[temp]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
if __name__=="__main__":
    G = Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(1,2)
    G.add_edge(2,0)
    G.add_edge(2,3)
    G.add_edge(3,3)

    print("BFS of graph starting from vertex 2")
    G.BFS(2)

''' TC = O(V+E)                            
