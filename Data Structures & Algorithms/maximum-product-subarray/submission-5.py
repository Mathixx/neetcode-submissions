class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = result = nums[0]
        for n in nums[1:]:
            candidates = (n, maxP * n, minP * n)
            maxP, minP = max(candidates), min(candidates)
            result = max(result, maxP)
        return result


        