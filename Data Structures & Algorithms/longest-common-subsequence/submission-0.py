class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            else:
                res = 0
                if i-1 > -1 and j-1 > -1 and text1[i-1] == text2[j-1]: 
                    res = max(res, dfs(i-1, j-1) + 1)
                if i-1 > -1: 
                    res = max(res, dfs(i-1, j))
                if j-1> -1:
                    res = max(res, dfs(i, j-1))
                dp[i][j] = res
                return res
        
        return dfs(m, n)


        