class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        result = ''
        
        for i in range(len(num1) - 1, -1, -1):
            c = 0
            curr_result = ''
            for j in range(len(num2) - 1, -1, -1):
                temp = int(num1[i]) * int(num2[j]) + c
                p = temp % 10
                c = temp // 10
                curr_result = str(p) + curr_result
            
            if c >= 1:
                curr_result = str(c) + curr_result
                
            curr_result += '0' * (len(num1) - 1 - i)
            result = self.add(result, curr_result)
        
        return result
        
        
    def add(self, num1: str, num2: str)-> str:
        
        if len(num1) > len(num2):
            num2 = (len(num1) - len(num2)) * '0' + num2
        elif len(num1) < len(num2):
            num1 = (len(num2) - len(num1)) * '0' + num1
        
        n = len(num1)
        
        result = ''
        c = 0
        
        for i in range(n-1, -1, -1):
            temp = int(num1[i]) + int(num2[i]) + c
            s = temp % 10
            c = temp // 10
            result = str(s) + result
        
        if c == 1:
            result = '1' + result
        
        return result
