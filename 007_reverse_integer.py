class Solution:
    def reverse(self, x: int) -> int:
        
        rev = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        
        return rev if -2**31 <= rev <= 2**31 - 1 else 0
    
