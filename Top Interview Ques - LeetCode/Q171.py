class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s) == 1:
            return ord(s[0])-64
        n = len(s)
        sum = 0
        for i in range(n-1):
            x = ord(s[i]) - 64
            sum += 26**(n-1-i)*x
        return sum + ord(s[-1]) - 64    
