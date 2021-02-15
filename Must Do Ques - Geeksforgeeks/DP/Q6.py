def lcs(m,n,X,Y):
    '''
    :param m: length of string X 
    :param n: length of string Y
    :param X: string X
    :param Y: string Y
    :return: Integer
    '''
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
