''' Disjoint Set (Or Union-Find) |
    Set 1 (Detect Cycle in an Undirected Graph)

    A disjoint-set data structure is a data structure that
    keeps track of a set of elements partitioned into a number
    of disjoint (non-overlapping) subsets.

     A union-find algorithm is an algorithm that performs two
     useful operations on such a data structure:

     Find: Determine which subset a particular element is in.
     This can be used for determining if two elements are in the same subset.

     Union: Join two subsets into a single subset.
'''

from collections import defaultdict

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent,parent[i])

    def union(self,parent,x,y):
        set_x = self.find_parent(parent,x)
        set_y = self.find_parent(parent,y)
        parent[set_x] = set_y

    def isCyclic(self):
        parent = [-1]*self.numVertex
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                if x == y :
                    return True
                self.union(parent,x,y)

if __name__=="__main__":
    G = Graph(3)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,0)
    if G.isCyclic():
        print("Graph has Cycle")
    else:
        print("Graph has no Cycle")                                                
