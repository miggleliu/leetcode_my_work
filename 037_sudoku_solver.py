class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # return a list containing all the possible valid digits for a grid
        def valid_digits(row, col):
            
            valid_digits = {1,2,3,4,5,6,7,8,9}
            
            # check rows and columns
            for i in range(9):
                if board[row][i] != '.' and int(board[row][i]) in valid_digits:
                    valid_digits.remove(int(board[row][i]))
                if board[i][col] != '.' and int(board[i][col]) in valid_digits:
                    valid_digits.remove(int(board[i][col]))
            
            # check subboxes
            row_s = row-row % 3
            col_s = col-col % 3
            
            for i in range(3):
                for j in range(3):
                    if board[row_s+i][col_s+j] != '.' and int(board[row_s+i][col_s+j]) in valid_digits:
                        valid_digits.remove(int(board[row_s+i][col_s+j]))
                    
            return valid_digits
        
        
        def solve(row, col):
            
            if col == 9:
                col = 0
                row += 1
            
            # reach the end, meaning that the solution is found
            if row == 9:
                return True
            
            # go to the next grid if the current grid is given by the question
            if board[row][col] != '.':
                return solve(row, col + 1)
  
            # DFS all possibilities
            valids = valid_digits(row, col)
            for i in valids:
                board[row][col] = str(i)
                if solve(row, col + 1):
                    return True
                
                # backtrack if False
                board[row][col] = '.'
            
            return False
        
        
        # main
        solve(0, 0)
        
