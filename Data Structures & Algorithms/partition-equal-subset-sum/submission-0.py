class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:return False

        # we know we want a non full subset whose sum is total//2
        dp = [[False]*(total//2+1) for _ in range(len(nums)+1)]
        dp[0][0] = True

        for i in range(1, len(nums)):
            for val in range(total//2+1):
                dp[i][val] |= dp[i-1][val]
                if val + nums[i-1] < total//2+1:
                    dp[i][val + nums[i-1]] |= dp[i-1][val]
        
        return dp[len(nums)-1][total//2]
    
    
    # def canPartition(self, nums: List[int]) -> bool:
    #     total = sum(nums)
    #     if total%2 == 1:return False

    #     # we know we want a non full subset whose sum is total//2
    #     memo = {}

    #     def dfs(i, target):
    #         if target < 1 or i < 0: return False
            
    #         if (i,target) in memo:
    #             return memo[(i, target)]
    #         else:
    #             if dfs(i-1, target-nums[i]) or dfs(i, target):
    #                 memo[(i, target)] = True
    #             else:
    #                 memo[(i, target)] = False
    #             return memo[(i, target)]
        
    #     return dfs(len(nums)-1, total//2)
