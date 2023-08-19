class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def safe(row,col,k,board): #function to check whether it is safe to insert a no. in board or not
            for i in range(9):
                if board[row][i]==k: # for checking element in same row
                    return False
                if board[i][col]==k: # for checking element in same column
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==k: # for checking element in same box
                    return False
            return True

        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if safe(i, j, str(k), board):
                                board[i][j] = str(k)
                                if backtrack(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        backtrack(board)            