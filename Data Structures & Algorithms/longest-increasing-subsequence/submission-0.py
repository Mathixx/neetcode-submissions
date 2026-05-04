class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        n = len(nums)
        dp = [1]*len(nums)
        dp[0] = 1
        longest = 0

        for i in range(1, n):
            res = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    res = max(res, 1+dp[j])
            dp[i] = res
            longest = max(longest, res)
        
        return longest
        
        