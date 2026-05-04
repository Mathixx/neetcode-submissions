class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_wtr = 0
        while l < r:
            h = min(heights[l], heights[r])
            max_wtr = max(max_wtr, h * (r - l))
            if h == heights[l]:
                l += 1
            else:
                r -= 1

        return max_wtr
        