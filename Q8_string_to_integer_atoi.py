class Solution:
    def myAtoi(self, str: str) -> int:
        
        str = str.strip()
        if not str:
            return 0
        
        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        i = 0
        while i < len(str) and str[i] in ['0','1','2','3','4','5','6','7','8','9']:
            i += 1
            
        str = int(str[:i]) * sign if i > 0 else 0

        if str < -2**31:
            return -2**31
        if str > 2**31 - 1:
            return 2**31 - 1
        return str
    
