class Solution:
	def maxSumIS(self, Arr, n):
		dp = [0]*n
		dp[0] = Arr[0]
		for i in range(1,n):
		    for j in range(i):
		        if Arr[i] > Arr[j]:
		            if dp[i] < dp[j] + Arr[i]:
		                dp[i] = dp[j] + Arr[i]
		        else:
		            dp[i] = max(dp[i],Arr[i])
		return max(dp)            
