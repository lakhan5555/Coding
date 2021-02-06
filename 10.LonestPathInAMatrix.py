''' Given a n*n matrix where all numbers are distinct, find the maximum length
path (starting from any cell) such that all cells along the path are in increasing
order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j)
 or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have
  a difference of 1.
'''

def findLongestFromACell(i,j,a,n,dp):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    x,y,z,w = -1,-1,-1,-1

    if (j < n-1) and (a[i][j] + 1) == a[i][j+1]:
        x = 1 + findLongestFromACell(i,j+1,a,n,dp)

    if (j > 0) and (a[i][j] + 1) == a[i][j-1]:
        y = 1 + findLongestFromACell(i,j-1,a,n,dp)

    if (i < n-1) and (a[i][j] + 1) == a[i+1][j]:
        z = 1 + findLongestFromACell(i+1,j,a,n,dp)

    if i > 0 and (a[i][j] + 1) == a[i-1][j]:
        w = 1 + findLongestFromACell(i-1,j,a,n,dp)

    dp[i][j] = max(1,x,y,z,w)
    return dp[i][j]

def findLongest(a,n):
    res = 1
    dp = [[-1 for col in range(n)] for row in range(n)]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                findLongestFromACell(i,j,a,n,dp)
            res = max(res,dp[i][j])
    return res

a = [[1,2,9],[5,3,8],[4,6,7]]
print("length of the longest path is: ",findLongest(a,3))


''' Time complexity of the above solution is O(n2). It may seem more at
first look. If we take a closer look, we can notice that all values of
 dp[i][j] are computed only once.
 '''
