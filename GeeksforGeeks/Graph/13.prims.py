''' Adjacency Matrix Representation '''
''' Greedy Algorithm '''

class Graph:
    def __init__(self,numVertex):
        self.numVertex = numVertex
        self.graph = [[0 for col in range(numVertex)]
                      for row in range(numVertex)]

    def printMST(self,parent):
        print("Edge \t Weight")
        for i in range(1,self.numVertex):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])

    def minKey(self,key,mstSet):
        min = float("inf")
        for v in range(self.numVertex):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_inx = v
        return min_inx

    def primMST(self):
        key = [float("inf")]*self.numVertex
        parent = [None]*self.numVertex

        key[0] = 0
        parent[0] = -1

        mstSet = [False]*self.numVertex

        for i in range(self.numVertex):
            u = self.minKey(key,mstSet)
            mstSet[u] = True

            for v in range(self.numVertex):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__=="__main__":
    g = Graph(5)
    g.graph = [[0,2,0,6,0],
               [2,0,3,8,5],
               [0,3,0,0,9],
               [6,8,0,0,9],
               [0,5,7,9,0]]
    g.primMST()


''' TC = O(V*2)  for adjacency matrix above
if we implement using adjacency list see -
  https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
'''
