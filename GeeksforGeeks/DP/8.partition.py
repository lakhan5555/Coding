'''
'''

'''
def partition(a,n):
    sum = 0
    for i in range(n):
        sum += a[i]

    if sum % 2 != 0:
        return False
    s = sum//2

    dp = [[True for i in range(n+1)]
            for j in range(s+1)]
    for i in range(1,s+1):
        dp[i][0] = False

    for i in range(1,s+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i][j-1]

            if i >= a[j-1]:
                dp[i][j] = dp[i][j] or dp[i-a[j-1]][j-1]
    return dp[s][n]

a = [1,5,11,5]
if partition(a,len(a)):
    print("can be partitioned")
else:
    print("can't partitioned")

'''
''' TC = O(n*sum)
SC = O(n*sum) '''

''' Space optimization '''

def partition(a,n):
    sum = 0
    for i in range(n):
        sum += a[i]

    if sum % 2 != 0:
        return False

    s = sum//2

    dp = [0]*(s+1)

    for i in range(n):
        for j in range(s,a[i]-1,-1):
            if dp[j-a[i]] == 1 or j == a[i]:
                dp[j] = 1
    return dp[s]

a = [1,5,11,5]
if partition(a,len(a)):
    print("can be partitioned")
else:
    print("can't partitioned")


''' TC = O(n*sum)
   SC = O(sum) '''
