class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n not in d:
                d[nums[i]] = i
            else:
                return [d[n],i]
        
