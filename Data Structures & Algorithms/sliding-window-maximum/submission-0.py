class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force doesn't work ?
        left = 0
        maxes = []
        while left + k < len(nums)+1:
            curr_max = max(nums[left:left+k])
            maxes.append(curr_max)
            left += 1
        
        return maxes

        