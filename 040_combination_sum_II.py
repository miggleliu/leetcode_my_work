# DFS, backtracking

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sort the candidates in decending order so that we can check the biggest element first
        # fill the bottle with stones firstly and sands lastly
        mp = {}.fromkeys(candidates, 0)
        for i in candidates:
            mp[i] += 1
        
        remain = sum(candidates)
        candidates = list(mp.keys())
        candidates.sort(reverse=True)
        ans = []
        
        def backtracking(idx, target, remain, mp, combination):
            
            # find a solution
            if target == 0:
                ans.append(combination)
                return
            
            # exceed the requirement
            if target < 0 or remain < target:
                return
            
            # if we do not pick the large element, we should not pick it afterwards. This is why we use variables idx and remain
            for i in range(idx, len(candidates)):
                
                if mp[candidates[i]] == 0:
                    continue
                    
                mp[candidates[i]] -= 1
                remain -= candidates[i]
                
                backtracking(i, target - candidates[i], remain, mp, combination + [candidates[i]])
                
                mp[candidates[i]] += 1
                
        
        # main
        backtracking(0, target, remain, mp, [])
        return ans
