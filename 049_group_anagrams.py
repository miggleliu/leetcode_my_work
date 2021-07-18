class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            sorted_s = self.sort_string(s)
            if sorted_s not in mp:
                mp[sorted_s] = [s]
            else:
                mp[sorted_s].append(s)
        
        return list(mp.values())
        

    def sort_string(self, s):
        lst = list(s)
        lst.sort()
        return ''.join(lst)
    
