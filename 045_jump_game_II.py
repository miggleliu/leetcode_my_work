class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # each jump should not exceed the length of nums
        for i in range(len(nums)):
            if nums[i] > len(nums) - i - 1:
                nums[i] = len(nums) - i - 1
        
        i = 0
        next = 0   # next is the next step we should take
        count = 0  # count is the total number of steps
        
        while i < len(nums) - 1:
            for j in range(i+1, i + nums[i] + 1):
                if j < len(nums) and nums[j] + j > nums[next] + next:
                    next = j
                 
            count += 1
            
            if next == i:
                return count  # reach the end (because there is always a solution)
            
            i = next
            
        return count
    
    
''' 
# dynamic programming; it works but takes unnecessarily much time.
class Solution:
    def jump(self, nums: List[int]) -> int:
    
        memo = {len(nums) - 1 : 0}
        
        def helper(i):
            # this function calculates the min number of jumps from index i
            if i in memo:
                return memo[i]

            if nums[i] == 0:
                memo[i] = math.inf
            elif i not in memo:
                memo[i] = min([helper(i + k) for k in range(1, min(len(nums) - i, nums[i] + 1))]) + 1
            return memo[i]
        
        helper(0)
        return memo[0]
'''
