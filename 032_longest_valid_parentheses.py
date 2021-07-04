# dynamic programming
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] -2] if i - dp[i - 1] -2 >= 0 else dp[i - 1] + 2
                ans = max(dp[i], ans)
        
        # print(dp)
        return ans


'''
# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

            
        return ans
'''

'''
# two pointers (constant memory, still linear time but more is needed)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        left = 0
        right = 0
        
        # scan from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if right > left:
                left = right = 0
            elif right == left:
                ans = max(ans, right * 2)
        
        # scan from right to left
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                left += 1
            else:
                right += 1
            
            if right > left:
                left = right = 0
            elif right == left:
                ans = max(ans, right * 2)
                
        return ans
'''
        
        
