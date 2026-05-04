class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        # Easy solution set() -> O(n) time and space
        # Mid : sort and iterate -> nlog(n) time O(1) space
        # Optimal: negate 0-indexed 
        for i in range(n+1):
            idx = abs(nums[i])-1
            if nums[idx] < 0:
                return idx + 1
            else:
                nums[idx] *= -1
        
        return 

        