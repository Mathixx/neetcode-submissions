from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        R, C = len(heights), len(heights[0])
        
        pac_queue = deque()
        atl_queue = deque()
        
        # 1. Fill queues with all boundary cells
        for r in range(R):
            pac_queue.append((r, 0))     # Left edge (Pacific)
            atl_queue.append((r, C - 1)) # Right edge (Atlantic)
        for c in range(C):
            pac_queue.append((0, c))     # Top edge (Pacific)
            atl_queue.append((R - 1, c)) # Bottom edge (Atlantic)

        def bfs(queue):
            reachable = set()
            while queue:
                r, c = queue.popleft()
                if (r, c) in reachable:
                    continue
                reachable.add((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # If inland cell is higher or equal, water can flow DOWN from it to here
                    if 0 <= nr < R and 0 <= nc < C and heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) not in reachable:
                            queue.append((nr, nc))
            return reachable

        # 2. Find all cells that can reach each ocean
        pac_reachable = bfs(pac_queue)
        atl_reachable = bfs(atl_queue)

        # 3. Intersection: cells in both sets
        return [list(cell) for cell in (pac_reachable & atl_reachable)]
            
            
            
        