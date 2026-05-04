class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        
        stack = [[temperatures[-1], n-1]]
        for i in range(n-2, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return result

        