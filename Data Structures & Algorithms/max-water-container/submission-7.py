# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         l, r = 0, len(heights)-1

#         max_wtr = 0
#         while l < r:
#             h = min(heights[l], heights[r])
#             max_wtr = max(max_wtr, h * (r - l))
#             if h == heights[r]:
#                 r -= 1
#             else:
#                 l += 1

#         return max_wtr

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_wtr = 0
        while l < r:
            h = min(heights[l], heights[r])
            max_wtr = max(max_wtr, h * (r - l))
            if h == heights[r]:
                r -= 1
            else:
                l += 1

        return max_wtr
        