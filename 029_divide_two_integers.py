'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        divisor_stack = []
        count_stack = []
        
        sum = 0
        count = 1
        
        while sum <= dividend - divisor:
            divisor_stack.append(divisor)
            count_stack.append(count)
            sum += divisor
            divisor += divisor
            count += count
        
        dividend -= sum
        
        while divisor_stack:
            divisor = divisor_stack.pop()
            count_temp = count_stack.pop()
            if divisor <= dividend:
                dividend -= divisor
                count += count_temp
                
        count -= 1
        
        if sign == 1:
            return count if count <= 2**31 - 1 else 2**31 - 1
        else:
            return -count if count >= -2**31 else -2**31
        
        # for example, to calculate 100/2, the procedure of the algorithm would be:
        # 100 = 2 + 4 + 8 + 16 + 32 + 32 + 4 + 2
        # count = 1 + (1 + 2 + 4 + 8 + 16 + 16 + 2 + 1) - 1
        # we use stacks to implement it in logn time complexity
'''

# Following the algorithm above, we can consider replacing the stack method with the shift operator in binary forms of the inputs. (Time complexity = O(logn))

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        count = 0
        
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                count += 1 << i
        
        if sign == 1:
            return count if count <= 2**31 - 1 else 2**31 - 1
        else:
            return -count if count >= -2**31 else -2**31
        
