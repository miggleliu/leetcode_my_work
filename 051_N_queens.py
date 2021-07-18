class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        def backtrack(row, remaining_cols, comb):
            if row == n:
                ans.append(comb.copy())
                return
                
            for i in range(len(remaining_cols)):
                # reduce column confliction
                col = remaining_cols[i]
                if col == -1:
                    continue
                    
                comb.append(col)
                
                if self.is_valid(comb):
                    remaining_cols[i] = -1
                    backtrack(row+1, remaining_cols, comb)
                    remaining_cols[i] = col
                    
                comb.pop()
                
                
        backtrack(0, list(range(n)), [])
        
        for comb in ans:
            for i in range(n):
                comb[i] = '.' * comb[i] + 'Q' + '.' * (n - comb[i] - 1)
        return ans
    
    
    # check diagonal validity
    def is_valid(self, comb):
        
        # check main diagonal
        main = []
        for i in range(len(comb)):
            if i - comb[i] not in main:
                main.append(i - comb[i])
            else:
                return False
        
        # check sub-diagonal
        sub = []
        for i in range(len(comb)):
            if i + comb[i] not in sub:
                sub.append(i + comb[i])
            else:
                return False
            
        return True
