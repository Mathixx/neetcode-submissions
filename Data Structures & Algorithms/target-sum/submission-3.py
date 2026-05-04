class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(int)
        dp[(0, -nums[0])] += 1
        dp[(0, nums[0])] += 1

        def dfs(i, target):
            if i < 0:
                return 0
            if (i, target) in dp:
                return dp[(i, target)]
            
            val = nums[i]
            dp[(i, target)] = dfs(i-1, target-val) + dfs(i-1, target+val)
            return dp[(i, target)]
        
        return dfs(len(nums)-1, target)
        