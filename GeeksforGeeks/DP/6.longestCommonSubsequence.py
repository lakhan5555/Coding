''' LCS Problem Statement: Given two sequences, find the length of longest subsequence
 present in both of them. A subsequence is a sequence that appears in the same
 relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”,
 ‘”acefg”, .. etc are subsequences of “abcdefg”.
 '''

''' Recursion '''
'''
def lcs(X,Y,m,n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is: ", lcs(X, Y,len(X),len(Y)))

TC = O(pow(2,n))

'''

''' DP '''

def lcs(X,Y):
    m = len(X)
    n = len(Y)
    t = [[None]*(n+1) for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif X[i-1] == Y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[m][n]

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of LCS is: ", lcs(X, Y))


''' TC = O(m*n) ''' 
