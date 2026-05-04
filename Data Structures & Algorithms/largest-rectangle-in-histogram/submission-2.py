class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1]*n
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] >= num:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i) 
        
        stack = []
        rightMost = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        largest = 0
        for i in range(n):
            l, r = leftMost[i] + 1, rightMost[i]-1
            largest = max(largest, heights[i] * (r - l + 1))
        return largest



        