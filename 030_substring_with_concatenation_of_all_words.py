class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        
        # create a dictionary to store the words
        mp = {}.fromkeys(words, 0)
        for word in words:
            mp[word] += 1
        
        each_len = len(words[0])
        total = each_len * len(words)
        i = 0
        
        for i in range(len(s) - total + 1):
            mp_copy = mp.copy()
            for j in range(i, i+total, each_len):
                curr = s[j:j+each_len]
                if curr in mp_copy and mp_copy[curr] > 0:
                    mp_copy[curr] -= 1
                else:
                    break
            else:
                # successfully match
                output.append(i)
            
        return output
