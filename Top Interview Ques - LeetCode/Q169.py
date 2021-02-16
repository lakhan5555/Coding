from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        a = int(n/2)
        d = defaultdict(int)
        for i in range(n):
            d[nums[i]] += 1
        for i in d:
            if d[i] > a:
                return i
        
