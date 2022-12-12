class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char.lower() for char in s if char.isalnum())
        temp = string[::-1]
        return temp == string