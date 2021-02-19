class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        r = 0
        for i in str(n):
            r += int(i)**2
        return self.isHappy(r)    
        
