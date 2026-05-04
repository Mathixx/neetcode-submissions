class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        minT = grid[n-1][n-1]
        heap = [(minT, n-1, n-1)]
        while heap:
            mint, i, j = heapq.heappop(heap)
            if i == 0 and j == 0:
                return mint
            visited[i][j] = True
            for n0, n1 in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if i+n0 < n and i+n0 > -1 and j+n1 < n and j+n1 > -1:
                    if not visited[i+n0][j+n1]:
                        t = max(mint, grid[i+n0][j+n1])
                        heapq.heappush(heap, (t, i+n0, j+n1))
        