class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        dp[-1] = 0

        def dynp(n):
            if n in dp:
                return dp[n]
            
            else:
                take = nums[n] + dynp(n-2)
                not_take = dynp(n-1)
                dp[n] = max(take, not_take)
                return dp[n]
        return dynp(len(nums)-1)
        