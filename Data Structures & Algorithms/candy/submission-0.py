class Solution:
    def candy(self, ratings: List[int]) -> int:
        memo = {}
        n = len(ratings)

        def dfs(i):
            if i in memo:
                return memo[i]
            
            candy = 0
            if i < n-1 and ratings[i] > ratings[i+1]:
                candy = max(dfs(i+1), candy)
            if i > 0 and ratings[i] > ratings[i-1]:
                candy = max(dfs(i-1), candy)
            
            memo[i] = candy + 1
            return candy + 1
        
        count = 0
        for i in range(n):
            count += dfs(i)
        
        return count

        