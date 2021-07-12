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



