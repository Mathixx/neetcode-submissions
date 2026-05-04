class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def backtrack(i, j, n, visited):
            if n == len(word): return True

            for u, v in DIR:
                ni, nj = u+i, v+j
                if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == word[n]:
                    if (ni, nj) in visited:
                        continue
                    else:
                        visited.add((ni, nj))
                        if backtrack(ni, nj, n+1, visited): return True
                        visited.remove((ni, nj))
            return False


        visited = set()

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if backtrack(i, j, 1, visited): return True
                    visited.remove((i, j))
        
        return False
        