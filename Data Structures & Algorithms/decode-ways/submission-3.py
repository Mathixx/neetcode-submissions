class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+2)
        dp[n], dp[n+1] = 1, 1
        

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i+1<n:
                    if s[i] == "1": dp[i] += dp[i+2]
                    elif s[i] == "2":
                        if s[i+1] in "0123456":
                            dp[i] += dp[i+2]

        return dp[0]



        