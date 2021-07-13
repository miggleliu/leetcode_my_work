'''
# recursion

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        # base case (len = 1)
        if len(candidates) == 1:
            
            # the candidates can satisfy the target
            if target % candidates[0] == 0:
                temp = []
                temp += [candidates[0]] * (target//candidates[0])
                return [temp]
            
            # the candidates cannot satisfy the target
            return None
        
        # go from the biggest candidate so as to reduce the number of searching
        max = target // candidates[-1]
        ans = []
        for i in range(max + 1):
            prev = self.combinationSum(candidates[:-1], target - i * candidates[-1])

            if not prev:
                continue
            
            # update the previous results
            for lst in prev:
                lst += [candidates[-1]] * i

            ans += prev
            
        return ans
'''


# DFS, backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sort the candidates in decending order so that we can check the biggest element first
        # fill the bottle with stones firstly and sands lastly
        candidates.sort(reverse=True)
        ans = []
        
        def backtracking(idx, target, combination):
            if target == 0:
                ans.append(combination.copy())
                return
            
            if target < 0:
                return
            
            # if we do not pick the large element, we cannot pick it afterwards. This is what idx is doing
            for i in range(idx, len(candidates)):
                backtracking(i, target - candidates[i], combination + [candidates[i]])
                
                
        backtracking(0, target, [])
        return ans
            
            
                
        
        

