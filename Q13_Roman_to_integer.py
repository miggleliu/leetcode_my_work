class Solution:
    def romanToInt(self, s: str) -> int:
        int = 0
        mp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i+1 < len(s) and mp[s[i+1]] > mp[s[i]]:
                int -= mp[s[i]]
            else:
                int += mp[s[i]]
        return int
            
