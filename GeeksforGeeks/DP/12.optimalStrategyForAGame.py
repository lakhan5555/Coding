def optimal(a):
    n = len(a)
    dp = [[0 for i in range(n)] for j in range(n)]
    for g in range(n):
        for j in range(g,n):
            i = j - g

            x = 0
            if (i + 2) <= j:
                x = dp[i+2][j]

            y = 0
            if (i+1) <= (j-1):
                y = dp[i+1][j-1]

            z = 0
            if i <= (j-2):
                z = dp[i][j-2]

            dp[i][j] = max(a[i] + min(x,y),a[j] + min(y,z))

    return dp[0][n-1]

if __name__=="__main__":
    a = [8,15,3,7]
    print("optimal solution: ",optimal(a))                        
