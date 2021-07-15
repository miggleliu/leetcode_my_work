class Solution:
    def trap(self, height: List[int]) -> int:
        
        vol = 0
        
        # traverse from left to right and find all the volumes whose left side is lower than its right side
        left = 0
        right = 0
        
        while left < len(height) - 2:
            for right in range(left + 1,len(height)):
                if height[right] > height[left]:
                    break
            else:
                break
                    
            vol += (right - left - 1) * height[left]
            for i in range(left + 1, right):
                vol -= height[i]
            
            left = right
            
        
        # traverse from right to left and find all the volumes whose right side is lower than its left side
        left_boundary = left
        
        right = len(height) - 1
        left = len(height) - 1
        
        while right > left_boundary + 1:
            for left in range(right - 1, -1, -1):
                if height[left] >= height[right]:
                    break
            else:
                break
                    
            vol += (right - left - 1) * height[right]
            for i in range(left + 1, right):
                vol -= height[i]
            
            right = left
        
        
        return vol
