class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_max = 0
        i = 0

        while i <= curr_max:
            if curr_max >= n-1:
                return True
            
            curr_max = max(curr_max, i + nums[i])
            i += 1
        
        return False

        