class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # convert all the non-positive ints into n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # find the number whose index (plus 1) is the value of the current number, and make it negative
        for i in nums:
            if abs(i) <= n:
                nums[abs(i)-1] = - abs(nums[abs(i)-1])
        
        # the index of the first positive number (plus 1) is the first missing positive int
        for i in range(n):
            if nums[i] > 0:
                return i+1
  
        return n + 1

