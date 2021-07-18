class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums]
        
        ans = []
        for i in range(len(nums)):
            nums_copy = nums.copy()
            curr = [nums_copy[i]]
            nums_copy.pop(i)
            for remain in self.permute(nums_copy):
                ans.append(curr + remain)

        return ans
        
            
