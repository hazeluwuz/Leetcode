class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        chars = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        openers = []
        for i in s:
            if i in chars:
                openers.append(i)
            else:
                if(len(openers) == 0):
                    return False
                temp = openers.pop()
                if chars[temp] != i:
                    return False
        return len(openers) == 0