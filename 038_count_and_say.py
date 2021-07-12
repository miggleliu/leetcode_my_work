class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'
        
        s = self.countAndSay(n-1)
        
        count = 1
        output = ''
        for i in range(len(s)):
            if i >= len(s) - 1 or s[i] != s[i+1]:
                output += str(count) + s[i]
                count = 1
            else:
                count += 1
        
        return output
        
