''' Given N X N matrix filled with 1, 0, 2, 3. Find whether there is a path
possible from source to destination, traversing through blank cells only.
You can traverse up, down, right, and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.

Note: there are an only a single source and single destination(sink). 
'''


from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s,d):
        if s == d:
            return True

        visited = [False]*(self.n*self.n + 1)

        q = []
        q.append(s)

        visited[s] = True

        while q:
            u = q.pop(0)

            for i in self.graph[u]:
                if i == d:
                    return True
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

        return False

def isSafe(i,j,mat):
    return i >=0 and i < len(mat) and j >= 0 and j < len(mat[0])

def findPath(mat):
    s,d = None, None
    N = len(mat)
    g = Graph(N)

    k = 1

    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0:
                if isSafe(i,j+1,mat):
                    g.add_edge(k,k+1)
                if isSafe(i,j-1,mat):
                    g.add_edge(k,k-1)
                if isSafe(i-1,j,mat):
                    g.add_edge(k,k-N)
                if isSafe(i+1,j,mat):
                    g.add_edge(k,k+N)

            if mat[i][j] == 1:
                s = k
            if mat[i][j] == 2:
                d = k
            k += 1
    return g.BFS(s,d)

if __name__=="__main__":
    M = [[0,3,0,1],
         [3,0,3,3],
         [2,3,3,3],
         [0,3,3,3]]

    if findPath(M):
        print("YES")
    else:
        print("NO")

''' TC = O(N*N) '''
