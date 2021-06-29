class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_s = math.inf
        
        for i in range(len(nums) - 2):
            # use two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if abs(s - target) < abs(closest_s - target):
                    closest_s = s

                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target
                
        return closest_s
