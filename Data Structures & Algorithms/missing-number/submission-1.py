class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for num in nums:
            missing ^= num
        
        full = 0
        for i in range(len(nums)+1):
            full ^= i
        
        return missing ^ full
        
