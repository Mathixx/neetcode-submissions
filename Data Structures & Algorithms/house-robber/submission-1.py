class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        dp[-1] = 0

        # def dynp(n):
        #     if n in dp:
        #         return dp[n]
            
        #     else:
        #         take = nums[n] + dynp(n-2)
        #         not_take = dynp(n-1)
        #         dp[n] = max(take, not_take)
        #         return dp[n]

        n = len(nums)
        for i in range(1, n):
            take = nums[i] + dp[i-2]
            not_take = dp[i-1]
            dp[i] = max(take, not_take)
            
        return dp[n-1]
        