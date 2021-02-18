class Solution:
        
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        def fn(a,index):
            if index < 0:
                a.insert(0,1)
                return

            a[index] = (a[index] + 1)%10
            if a[index] == 0:
                fn(a,index-1)
        fn(digits,n-1)  
        return digits
            
