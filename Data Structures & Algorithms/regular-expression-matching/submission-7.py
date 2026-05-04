class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if j == len(p): 
                return i == len(s)
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")
            
            res = False 

            if j + 1 < len(p) and p[j+1] == "*":
                res = dfs(i, j+2)
                if first_match:
                    res |= dfs(i+1, j)
            
            else:
                if first_match:
                    res = dfs(i+1, j+1)
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)