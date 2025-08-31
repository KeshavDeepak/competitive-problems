class Solution:
    def check_row(self, board, row, column):
        number = board[row][column]
        
        for (column_index, element) in enumerate(board[row]):
            if column_index == column: continue
            
            
            
            if element == number: return False
        
        return True

    def check_column(self, board, row, column):
        number = board[row][column]
        
        for row_index in range(9):
            if row_index == row: continue
            
            element = board[row_index][column]
            
            if element == number: return False
        
        return True
        
    def check_subgrid(self, board, row, column):
        curr_row = row - (row % 3)
        curr_col = column - (column % 3)
        
        number = board[row][column]
        
        for i in range(3):
            for j in range(3):
                if (curr_row, curr_col) == (row, column): continue
                
                if board[curr_row][curr_col] == number: return False
                
                curr_col += 1
            
            curr_row += 1
            curr_col = column - (column % 3)
        
        return True

    def cell_is_valid(self, board, row, column):
        return self.check_row(board, row, column) and \
               self.check_column(board, row, column) and \
               self.check_subgrid(board, row, column)
               
        # return self.check_row(board, row, column)
               
        # return self.check_column(board, row, column)
               
        # return self.check_subgrid(board, row, column)
        
        
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                
                if not self.cell_is_valid(board, i, j): return False
        
        return True

# main code
solution = Solution()

# test case 1
print(solution.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))