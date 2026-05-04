class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dict_profit = {}
        n = len(prices)

        def dfs(i, can_buy):
            if i > len(prices)-1:
                return 0

            if (i, can_buy) in dict_profit:
                return dict_profit[(i, can_buy)]
            
            next_day = dfs(i+1, can_buy)
            if can_buy:
                buy = dfs(i+1, False) - prices[i]

                dict_profit[(i, can_buy)] = max(next_day, buy)
            else:
                sell = dfs(i+2, True) + prices[i]

                dict_profit[(i, can_buy)] = max(next_day, sell)
            return dict_profit[(i, can_buy)]
        
        return dfs(0, True)


        