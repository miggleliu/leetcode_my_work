class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # binary search
        low = 0
        high = len(nums) - 1
        middle = (low + high) // 2
        
        if target <= nums[0]:
            return 0
        
        while low <= high:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
                middle = int((low + high) / 2)
            else:
                high = middle - 1
                middle = int((low + high) / 2)
        
        # if cannot find
        if nums[middle] > target:
            return middle - 1
        else:
            return middle + 1
