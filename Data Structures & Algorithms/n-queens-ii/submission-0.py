class Solution:
    def checkboard(self, board, row, column):
        # Running in O(n)
        # Check if adding a queen at row and column makes it unvalid
        n = len(board)
        left = (row-1, column-1)
        right = (row-1, column+1)
        while left or right:
            if left:
                if left[0] > -1 and left[1] > -1:
                    if board[left[0]][left[1]]:
                        return False
                    left = (left[0]-1, left[1]-1)
                else:
                    left = None
            if right:
                if right[0] > -1 and right[1] < n:
                    if board[right[0]][right[1]]:
                        return False
                    right = (right[0]-1, right[1]+1)
                else: 
                    right = None
        return True
    
    def totalNQueens(self, n: int) -> int:
        count = 0
        used_column = set()

        board = [[False] * n for _ in range(n)]

        def backtrack(board, row, used_column):
            if row == n:
                return 1
            
            count = 0
            for i in range(n):
                if i in used_column:
                    continue
                else:
                    board[row][i] = True
                    used_column.add(i)
                    valid = self.checkboard(board, row, i)
                    # Check if board is valid
                    if valid:
                        count += backtrack(board, row+1, used_column)
                    board[row][i] = False
                    used_column.remove(i)
            
            return count
        
        return backtrack(board, 0, used_column)


        


        
        