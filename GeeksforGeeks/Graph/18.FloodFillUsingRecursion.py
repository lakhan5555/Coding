''' Given a 2D screen, location of a pixel in the screen and a color,
replace color of the given pixel and all adjacent same colored pixels
with the given color.
'''

def floodFillUtil(screen,x,y,prevC,newC, N, M):
    if x < 0 or x >= N or y < 0 or y >= M or screen[x][y] != prevC or screen[x][y] == newC:
        return

    screen[x][y] = newC

    floodFillUtil(screen,x+1,y,prevC,newC,N,M)
    floodFillUtil(screen,x-1,y,prevC,newC,N,M)
    floodFillUtil(screen,x,y+1,prevC,newC,N,M)
    floodFillUtil(screen,x,y-1,prevC,newC,N,M)

def floodFill(screen,x,y,newC,N,M):
    prevC = screen[x][y]

    floodFillUtil(screen,x,y,prevC,newC,N,M)

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

    newC = 3

    floodFill(screen,x,y,newC,8,8)

    print("Updated screen after floodFill: ")

    for i in range(8):
        for j in range(8):
            print(screen[i][j],end=" ")
        print()


''' Since each cell can be reached 4 times and no. of cells = N*M
so TC = O(4*N*M) = O(N*M)
'''
