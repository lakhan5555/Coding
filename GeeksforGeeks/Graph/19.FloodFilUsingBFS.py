''' Given a 2D screen, location of a pixel in the screen and a color,
 replace color of the given pixel and all adjacent same colored pixels
 with the given color.
 '''

def isValid(x,y,n,m):
     return x >= 0 and x < n and y >= 0 and y < m

def BFS(screen,x,y,color,n,m):
    visited = [[False for col in range(m)]
                for row in range(n)]

    q = []

    q.append((x,y))
    visited[x][y] = True
    preColor = screen[x][y]

    while q:
        v = q.pop(0)
        i,j  = v

        screen[i][j] = color

        if isValid(i+1,j,n,m) and not visited[i+1][j] and screen[i+1][j] == preColor:
            q.append((i+1,j))
            visited[i+1][j] = True

        if isValid(i-1,j,n,m) and not visited[i-1][j] and screen[i-1][j] == preColor:
            q.append((i-1,j))
            visited[i-1][j] = True

        if isValid(i,j+1,n,m) and not visited[i][j+1] and screen[i][j+1] == preColor:
            q.append((i,j+1))
            visited[i][j+1] = True

        if isValid(i,j-1,n,m) and not visited[i][j-1] and screen[i][j-1] == preColor:
            q.append((i,j-1))
            visited[i][j-1] = True

if __name__=="__main__":
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

    x = 4
    y = 4

    color = 3

    BFS(screen,x,y,color,8,8)

    print("Updated screen after floodFill: ")

    for i in range(8):
        for j in range(8):
            print(screen[i][j],end=" ")
        print()
