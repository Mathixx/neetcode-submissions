class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = n-1
        max_p = 0
        min_b = prices[left]
        for p in prices:
            if p < min_b:
                min_b = p
            else:
                profit = p - min_b
                max_p = max(max_p, profit)
        return max_p


        