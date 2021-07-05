# check for rows, columns and boxes respectively
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check validity for rows
        for row in board:
            t = set()
            for i in row:
                if i != '.':
                    if i in t:
                        return False
                    t.add(i)

        # check validity for columns
        for idx in range(9):
            t = set()
            for row in board:
                if row[idx] != '.':
                    if row[idx] in t:
                        return False
                    t.add(row[idx])
        
        # check validity for boxes
        for i in [0,3,6]:
            for j in [0,3,6]:
                t = set()
                for row in [i, i+1, i+2]:
                    for col in [j, j+1, j+2]:
                        if board[row][col] != '.':
                            if board[row][col] in t:
                                return False
                            t.add(board[row][col])
                            
        return True
        
