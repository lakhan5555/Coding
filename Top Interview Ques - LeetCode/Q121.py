class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_p = float("inf")
        max_p = 0
        for i in range(n):
            if min_p > prices[i]:
                min_p = prices[i]
            elif (prices[i] - min_p) > max_p :
                max_p = prices[i] - min_p
        return max_p        
        
