class Solution:
    def minOperation(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n % 2 == 0:
            return self.minOperation(int(n/2)) + 1
        else:
            return self.minOperation(int(n/2)) + 2
