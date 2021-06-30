class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_v = 0
        
        while start < end:
            v = min(height[start],height[end]) * (end - start)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
                
            if v > max_v:
                max_v = v
        
        return max_v
