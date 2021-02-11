''' Given a MxN matrix where each element can either be 0 or 1. We need to
find the shortest path between a given source cell to a destination cell.
The path can only be created out of a cell if its value is 1.
'''

class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

class qNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist

class ShortedPath:
    def __init__(self,ROW,COL):
        self.ROW = ROW
        self.COL = COL

    def isValid(self,row: int, col: int):
        return row >= 0 and row < self.ROW and col >= 0 and col < self.COL

    def BFS(self,mat, src: Point, dest: Point):
        if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
            return -1

        visited = [[False for i in range(self.COL)]
                      for j in range(self.ROW)]

        visited[src.x][src.y] = True

        rowNum = [-1,0,0,1]
        colNum = [0,-1,1,0]

        q = []

        s = qNode(src,0)
        q.append(s)

        while q:
            curr = q.pop(0)

            pt = curr.pt

            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]

                if self.isValid(row,col) and mat[row][col] == 1 and not visited[row][col]:
                    visited[row][col] = True
                    adjCell = qNode(Point(row,col),curr.dist+1)
                    q.append(adjCell)
        return -1

if __name__=="__main__":
    mat = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
           [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
           [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
           [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
    r = 9
    c = 10

    src = Point(0,0)
    dest = Point(3,4)

    d = ShortedPath(r,c)
    dist = d.BFS(mat,src,dest)

    if dist != -1:
        print("shortest path is: ",dist)
    else:
        print("shortest path doesn't exist")


''' TC = O(N*M)
