class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m, n = len(s), len(wordDict)
        dp = [False]*(m+1)
        dp[0] = True

        for i in range(1, m+1):
            res = False
            for w in wordDict:
                if res: break
                l = len(w)
                if i >= l and s[i-l:i] == w:
                    res |= dp[i-l]
        
            dp[i] = res
        
        return dp[m]
                
        