class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        ans = []
        
        if not digits:
            return []
        if len(digits) == 1:
            return dic[digits[0]]
        
        # use recursion to solve the problem
        for i in dic[digits[-1]]:
            for j in self.letterCombinations(digits[:-1]):
                ans.append(j+i)
                
        return ans
