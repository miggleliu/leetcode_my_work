class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {'(':0, ')':0, '[':1, ']':1, '{':2, '}':2}

        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if stack:
                    if dic[i] != dic[stack.pop()]:
                        return False
                else:
                    return False
        return stack == []
        
        '''
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
        '''
