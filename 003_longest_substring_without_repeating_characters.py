class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict()
        
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            if s[end] in mp:
                start = max(start, mp[s[end]] + 1)
            
            mp[s[end]] = end 
            max_len = max(end - start + 1, max_len)
            end += 1
            
        return max_len
