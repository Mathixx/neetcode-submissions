class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0
        buy_idx = 0
        while buy_idx + 1 < n:
            if prices[buy_idx] < prices[buy_idx+1]:
                profit += prices[buy_idx+1] - prices[buy_idx]
            buy_idx+=1
        
        return profit
        