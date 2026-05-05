class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(int)
        
        def dynp(s_i, t_i):
            if (s_i, t_i) in dp:
                return dp[(s_i, t_i)]
            if t_i == -1:return 1
            if s_i == -1: return 0
            
            if s[s_i] == t[t_i]:
                dp[(s_i, t_i)] += dynp(s_i-1, t_i-1)
            dp[(s_i, t_i)] += dynp(s_i-1, t_i)
            return dp[(s_i, t_i)]

        return dynp(len(s)-1, len(t)-1)
        