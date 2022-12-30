class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        
        for i in magazine:
            if i not in chars:
                chars[i] = 1
            else:
                chars[i] += 1
        
        for i in ransomNote:
            if i not in chars or chars[i] < 1:
                return False
            else:
                chars[i]-=1
        
        return True