class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # To avoid p from ending with '*'. The result won't change.
        s += 'a'
        p += 'a'
        
        # dynamic programming
        memo = {}
        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # base case
            if i == len(s) and j == len(p):
                memo[(i, j)] = True
            elif i == len(s) and j < len(p) or i < len(s) and j == len(p):
                memo[(i, j)] = False
            
            # recursion
            elif s[i] == p[j] or p[j] == '?' and i < len(s):
                memo[(i, j)] = helper(i+1, j+1)
            elif p[j] == '*':
                memo[(i, j)] = helper(i, j+1) or helper(i+1, j)
                
            else:
                memo[(i, j)] = False
                
            return memo[(i, j)]
        
        # main
        helper(0, 0)
        return memo[(0,0)]

