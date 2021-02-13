def ceil(t,l,r,key):
    while r - l > 1:
        m = l + int((r-l)/2)
        if key <= t[m]:
            r = m
        else:
            l = m
    return r        
    
def longestSubsequence(a,n):
    # l = [1]*n
    # for i in range(1,n):
    #     for j in range(i):
    #         if a[i] > a[j] and l[i] < l[j] + 1:
    #             l[i] = l[j] + 1
    # return max(l)            

    t = [0 for i in range(n+1)]
    t[0] = a[0]
    len = 1
    
    for i in range(1,n):
        if a[i] < t[0]:
            t[0] = a[i]
        elif a[i] > t[len-1]:
            t[len] = a[i]
            len += 1
        else:
            t[ceil(t,-1,len-1,a[i])] = a[i]
    return len        
