class Solution:
    def trap(self, height: List[int]) -> int:
        # leftMost array and rightMost array and 
        # at each position you add how much water and that max(0, min(leftMost, rightMost)- level
        
        leftMost = [0]
        currMax = 0 
        for i in range(len(height)-1):
            currMax = max(currMax, height[i])
            leftMost.append(currMax)

        rightMost = [0]
        currMax = 0
        for i in range(len(height)-1, 0, -1):
            currMax = max(currMax, height[i])
            rightMost.append(currMax)
        rightMost = rightMost[::-1]

        trapped = 0
        for i in range(len(height)):
            trapped += max(0, min(leftMost[i], rightMost[i])-height[i])

        return trapped


