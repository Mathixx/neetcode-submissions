class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinPrice = float('inf')
        profit = 0
        l = 0
        while l < len(prices):
            if prices[l] > currMinPrice:
                profit += prices[l] - currMinPrice
                currMinPrice = prices[l]
            else:
                currMinPrice = prices[l]
            l+=1
        return profit


        