class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_so_far = nums[0]

        n = len(nums)
        for i in range(1,n):
            curr_max = max(nums[i],curr_max+nums[i])
            max_so_far = max(max_so_far,curr_max)
        return max_so_far    
