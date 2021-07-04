class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums[0]
        if target == pivot:
            return 0
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            logic = (target >= nums[mid]) ^ (nums[mid] >= pivot) ^ (pivot >= target)
            if logic:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
            
# The logic is concluded from the following observations:
# if target >= nums[mid] >= pivot: 
#     left = mid + 1
# elif nums[mid] >= target >= pivot:
#     right = mid - 1
# elif target >= pivot >= nums[mid]:
#     right = mid - 1
# elif nums[mid] >= pivot >= target:
#     left = mid + 1
# elif pivot >= target >= nums[mid]:
#     left = mid + 1
# elif pivot >= nums[mid] >= target:
#     right = mid - 1
                       
