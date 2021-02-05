''' The Longest Increasing Subsequence (LIS) problem is to find the length of the
 longest subsequence of a given sequence such that all elements of the subsequence
 are sorted in increasing order.
'''

def lonIncreSubse(a,n):
    l = [1]*n
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    return max(l)

if __name__=="__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is: ", lonIncreSubse(arr,len(arr)))

''' TC = O(n*2)
SC = O(n) '''
