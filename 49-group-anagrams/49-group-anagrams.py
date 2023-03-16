class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        
        for i in strs:
            s = "".join(sorted(i))
            if s in dct:
                dct[s].append(i)
            else:
                dct[s] = [i]
        return dct.values()