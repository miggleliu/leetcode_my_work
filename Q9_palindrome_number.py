class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)[::-1] == str(x)
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while rev < x:
            rev = rev * 10 + x % 10
            x = x//10
        
        return rev == x or rev//10 == x
                
