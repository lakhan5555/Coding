''' doing LIS in O(nlogn) '''

def ceil(t,l,r,key):
    while r - l > 1:
        m = l + int((r-l)/2)
        if key <= t[m]:
            r = m
        else:
            l = m
    return r


def longestSubsequence(a,n):

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

if __name__=="__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is: ", longestSubsequence(arr,len(arr)))    
