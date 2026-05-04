class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        # Base case: we successfully reached "before the start" of the string
        dp = {-1: True}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = False
            for w in wordDict:
                l = len(w)
                # Check if the word fits and matches the substring ending at 'i'
                # The slice s[i-l+1 : i+1] gets the word ending exactly at i
                if i - l + 1 >= 0 and s[i-l+1 : i+1] == w:
                    if dfs(i - l): # If the previous part of the string works
                        res = True
                        break
            
            dp[i] = res
            return res
        
        # Start the recursion from the last index of the string
        return dfs(len(s) - 1)
            

        