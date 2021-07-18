class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums]
        
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i >= 1 and nums[i - 1] == nums[i]:
                continue
            nums_copy = nums.copy()
            curr = [nums_copy[i]]
            nums_copy.pop(i)
            for remain in self.permuteUnique(nums_copy):
                ans.append(curr + remain)

        return ans
