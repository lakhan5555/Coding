''' Given a connected and undirected graph, a spanning tree of that graph is a
subgraph that is a tree and connects all the vertices together. A single graph
 can have many different spanning trees. A minimum spanning tree (MST) or
 minimum weight spanning tree for a weighted, connected and undirected graph
 is a spanning tree with weight less than or equal to the weight of every
 other spanning tree. The weight of a spanning tree is the sum of weights given to
 each edge of the spanning tree.

 How many edges does a minimum spanning tree has?
 A minimum spanning tree has (V – 1) edges where V is
 the number of vertices in the given graph.
 '''

 ''' Greedy algorithm '''

class Graph:
    def __init__(self,numVertex):
         self.numVertex = numVertex
         self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find_parent(self,parent,i):
        if parent[i] == i:
            return i
        return self.find_parent(parent,parent[i])

    def union(self,parent,rank,x,y):
        set_x = self.find_parent(parent,x)
        set_y = self.find_parent(parent,y)

        if rank[set_x] > rank[set_y]:
            parent[set_y] = set_x
        elif rank[set_y] > rank[set_x]:
            parent[set_x] = set_y
        else:
            parent[set_y] = set_x
            rank[set_x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph,key = lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.numVertex):
            parent.append(node)
            rank.append(0)

        while e < self.numVertex - 1:
            u,v,w = self.graph[i]
            i += 1
            x = self.find_parent(parent,u)
            y = self.find_parent(parent,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent,rank,x,y)

        minCost = 0
        print("edges in the constructed MST is: ")
        for u,v,w in result:
            minCost += w
            print("%d -- %d == %d"%(u,v,w))
        print("MST: ",minCost)

if __name__=="__main__":
    g = Graph(4)
    g.add_edge(0,1,10)
    g.add_edge(0,2,6)
    g.add_edge(0,3,5)
    g.add_edge(1,3,15)
    g.add_edge(2,3,4)

    g.KruskalMST()


''' Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time
. After sorting, we iterate through all edges and apply find-union algorithm.
 The find and union operations can take atmost O(LogV) time. So overall
 complexity is O(ELogE + ELogV) time. The value of E can be atmost O(V2),
 so O(LogV) are O(LogE) same. Therefore, overall time complexity is O(ElogE)
  or O(ElogV) '''
