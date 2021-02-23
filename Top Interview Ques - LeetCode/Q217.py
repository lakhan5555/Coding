from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        n = len(nums)
        for x in nums:
            if d[x] >= 1:
                return True
            else:
                d[x] += 1
        return False        
  
