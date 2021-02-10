''' Union-Find Algorithm | Set 2 (Union By Rank and Path Compression)

    Following is union by rank and path compression based implementation
    to find a cycle in a graph.

    https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
'''

from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

class Subset:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

def find(subsets,node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets,subsets[node].parent)
    return subsets[node].parent

def union(subsets,u,v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

def isCyclic(g):
    subsets = []

    for u in range(g.numVertex):
        subsets.append(Subset(u,0))

    for u in g.graph:
        x = find(subsets,u)
        for v in g.graph[u]:
            y = find(subsets,v)
            if x == y:
                return True
            union(subsets,x,y)

if __name__=="__main__":
    G = Graph(3)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,0)
    if isCyclic(G):
        print("Graph has Cycle")
    else:
        print("Graph has no Cycle")
