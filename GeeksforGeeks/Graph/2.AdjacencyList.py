class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = [None]*numVertex

    def add_edge(self,src,dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # don't do this for directed graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.numVertex):
            print("Adjacency list of vertex {} \n head".format(i),end=" ")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex),end=" ")
                temp = temp.next
            print()

if __name__=="__main__":
    G = Graph(5)
    G.add_edge(0,1)
    G.add_edge(0,4)
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(2,3)
    G.add_edge(3,4)

    G.print_graph()
