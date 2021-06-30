class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ''
        b = True
        minlen = len(strs[0])
        char = 0

        for each in strs:
            minlen = len(each) if minlen > len(each) else minlen

        while b and char < minlen:
            for i in range(1, len(strs)):
                if strs[i][char] != strs[i-1][char]:
                    b = False
                    break
                    
            common += strs[0][char] if b else ''
            char += 1

        return common

        # return os.path.commonprefix(strs)
            
