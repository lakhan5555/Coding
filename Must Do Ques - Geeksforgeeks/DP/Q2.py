def maxChainLen(Parr, n):
    
    ''' Gready '''
    # a = []
    # for x in Parr:
    #     a.append([x.a,x.b])
    # a.sort(key = lambda x: x[1])
    # count = 1
    # i = 0
    # for j in range(1,n):
    #     if a[j][0] > a[i][1] :
    #         count += 1
    #         i = j
    # return count
    
    ''' DP '''
    m = [1 for x in range(n)]
    a = []
    for x in Parr:
        a.append([x.a,x.b])
    a.sort(key = lambda x: x[0])
    
    for i in range(1,n):
        for j in range(i):
            if a[i][0] > a[j][1] and m[i] < m[j] + 1:
                m[i] = m[j] + 1
    return max(m) 
