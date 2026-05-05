class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1][1]
            stack.append((heights[i], i))
        
        stack = []
        rightMost = [n] * n
        for i in range(len(heights)-1,-1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] =stack[-1][1]

            stack.append((heights[i], i))

        largest = 0
        for i in range(n):
            largest = max(largest, heights[i] * (rightMost[i]-leftMost[i] - 1))
        
        return largest
        