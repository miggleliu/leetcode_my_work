class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # method 1 (backtrack)
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        
        backtrack()
        return ans

'''
# method 2 (closure number)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for x in range(n):
            for left in self.generateParenthesis(x):
                for right in self.generateParenthesis(n-1-x):
                    ans.append('('+left+')'+right)
        
        return ans
'''
