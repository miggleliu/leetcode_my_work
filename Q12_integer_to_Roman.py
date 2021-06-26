class Solution:
    def intToRoman(self, num: int) -> str:
        rom = ''
        one = {0:'I', 1:'X', 2:'C', 3:'M'}
        five = {0:'V', 1:'L', 2:'D'}
        p = 3
        
        while num > 0 and p >= 0:
            d = num//(10**p)
            if d == 0:
                p -= 1
                continue
            elif d < 4:
                rom += one[p] * d
            elif d == 4:
                rom += one[p] + five[p]
            elif d < 9 :
                rom += five[p] + one[p]*(d-5)
            else:
                rom += one[p] + one[p+1]
            
            num -= d*10**p
            p -= 1
            
        return rom
