class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # two pointers to haystack and needle respectively
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i] != needle[j]:
                    break
                i += 1
            else:
                return i - len(needle)
            
        return -1
