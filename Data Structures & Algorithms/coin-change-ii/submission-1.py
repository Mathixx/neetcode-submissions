class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(i, current_amount):
            if current_amount == 0:
                return 1
            
            if current_amount < 0 or i < 0:
                return 0
            
            if dp[i][current_amount] != -1:
                return dp[i][current_amount]
            
            exclude = dfs(i - 1, current_amount)
            include = dfs(i, current_amount - coins[i])
            
            dp[i][current_amount] = exclude + include
            return dp[i][current_amount]

        return dfs(len(coins) - 1, amount)