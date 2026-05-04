class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_set = set(range(0,len(nums)+1))
        for num in nums:
            full_set.remove(num)
        for key in full_set:
            return key
        