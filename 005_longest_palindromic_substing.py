class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        if s == '':
            return ''
        elif len(s) == 1:
            return s[0]
        else:
            maxs = s[0]
            indices = {}
            for idx, char in enumerate(s):
                indices.setdefault(char,[]).append(idx)
            for lst in indices.values():
                if len(lst) == 1:
                    continue
                else:
                    for i in range(len(lst)):
                        for j in range(i+1, len(lst)):
                            cur = s[lst[i]:lst[j]+1]
                            if cur == cur[::-1]:
                                if len(cur) > len(maxs):
                                    maxs = cur
            return maxs
            '''
        
        # Manacher's ALGORITHM
        if s == '':
            return ''
        elif len(s) == 1:
            return s[0]

        s1 = '$'+'$'.join(s)+'$'
        cur = 0
        right = 0
        center = 0
        l = len(s1)
        cur_l = [0] * l
        max_s = 0

        while cur < l and right < l:
            if cur >= right:
                i = 1
                while cur - i >= 0 and cur + i <= l - 1:
                    if s1[cur-i] == s1[cur+i]:
                        cur_l[cur] += 1
                        i += 1
                    else:
                        break
                right = cur + i - 1
                center = cur
            else:
                cur_l[cur] = min(cur_l[2*center-cur], right-cur)
                if cur_l[cur] == right-cur:
                    i = right - cur + 1
                    while cur - i >= 0 and cur + i <= l - 1:
                        if s1[cur-i] == s1[cur+i]:
                            cur_l[cur] += 1
                            i += 1
                        else:
                            break
                    if cur + i - 1 > right:
                        right = cur + i - 1
                        center = cur
                        
            cur += 1

        max_l = max(cur_l)
        idx = cur_l.index(max_l)
        idx = (idx-1)/2
        bottom = int(idx - (max_l - 1)/2)
        up = int(idx + (max_l - 1)/2)

        return s[bottom:up+1]
