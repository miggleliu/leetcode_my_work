class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_left_boundary(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.search_right_boundary(nums[left:], target) + left
        return [left, right]
        
        
    def search_left_boundary(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                return mid
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
    
    def search_right_boundary(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] != target):
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
