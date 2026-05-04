class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [ [0, 0] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        dp[1][0], dp[1][1] = nums[1], dp[0][1]

        for i in range(2, n):
            if i == n-1:
                dp[i][1] = dp[i-1][1]
                dp[i][0] = max(dp[i-2][0] + nums[i], dp[i-1][0])
            else:
                dp[i][0] = max(dp[i-2][0] + nums[i], dp[i-1][0])
                dp[i][1] = max(dp[i-2][1] + nums[i], dp[i-1][1])
        
        return max(dp[n-1][0], dp[n-1][1])
        
