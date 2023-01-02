class Solution:
    def longestPalindrome(self, s: str) -> int:
        words = set()
        
        for c in s:
            if c not in words:
                words.add(c)
            else:
                words.remove(c)
        
        return len(s) - len(words) + 1 if len(words) > 0 else len(s)