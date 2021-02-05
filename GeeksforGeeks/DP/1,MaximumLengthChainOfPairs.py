''' You are given n pairs of numbers. In every pair, the first number is always smaller
 than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain
 of pairs can be formed in this fashion. Find the longest chain which can be formed
 from a given set of pairs. 
'''

''' Bottom Up Approach - Tabulation approach '''

class Pair:
    def __init__(self,a,b):
        self.a = a
        self.b = b

def MaxLen(Parr,n):
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

if __name__=="__main__":
    Parr = [Pair(5,24),Pair(39,60),Pair(15,28),Pair(27,40),Pair(50,90)]
    print(MaxLen(Parr,len(Parr)))


''' TC = O(n*2)
 can be solved in O(n*logn) with Greedy '''
