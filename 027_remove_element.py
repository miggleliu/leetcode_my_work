class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i

    
'''
# if the elements to be removed are rare, swap instead of copy.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
                
        return n
'''
