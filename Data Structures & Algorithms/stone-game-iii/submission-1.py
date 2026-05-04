class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] represents the max score Alice can get starting from index i
        # We use n + 3 to avoid index out of bounds during the loop
        dp = [0] * (n + 3)
        
        # Pre-calculate suffix sums to avoid repeated summing
        # suffix_sum[i] = sum(stoneValue[i:])
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

        # Fill DP table backwards
        for i in range(n - 1, -1, -1):
            res = suffix_sum[i] - dp[i + 1]
            
            if i + 1 < n:
                res = max(res, suffix_sum[i] - dp[i + 2])
            
            # Option 3: Take 3 stones
            if i + 2 < n:
                res = max(res, suffix_sum[i] - dp[i + 3])
            
            dp[i] = res

        alice_sum = dp[0]
        total_sum = suffix_sum[0]

        # Final comparison logic
        # Note: Be careful with // 2 on odd sums; comparing directly is safer
        if alice_sum * 2 > total_sum:
            return "Alice"
        elif alice_sum * 2 == total_sum:
            return "Tie"
        else:
            return "Bob"
        

            
        