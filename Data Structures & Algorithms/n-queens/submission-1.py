class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(board, i, j):
            # Assuming board is valid
            # Check wether you can add quen in i,j or not
            if "Q" in board[i]:
                return False
            for line in range(n):
                if board[line][j] == "Q":
                    return False
            
            diags = [(-1,1),(1,1), (-1,-1),(1,-1)]
            for k in range(1, n):
                if not diags:
                    break
                new_diags = []
                while diags:
                    di, dj = diags.pop()
                    if i+di*k>n-1 or i+di*k<0 or j+dj*k<0 or j+dj*k>n-1:
                        continue
                    else:
                        if board[i+di*k][j+dj*k] == "Q":
                            return False
                        new_diags.append((di, dj))
                diags = new_diags
            
            return True

        res = []
        def backtrack(board, line):
            if line == n:
                res.append(board.copy())
                return
            else:
                for col in range(n):
                    if valid(board, line, col):
                        board[line] = col*"." + "Q" + "."*(n-col-1)
                        backtrack(board, line+1)
                        board[line] = "."*n

        board = ["."*n for _ in range(n)]
        backtrack(board, 0)
        return res


        
                    




                
