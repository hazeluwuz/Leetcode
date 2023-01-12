class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            valid_word = True
            temp_chars = list(chars)
            for c in word:
                if c not in temp_chars:
                    valid_word = False
                    break
                else:
                    temp_chars.remove(c)
            print(temp_chars, word)
            if valid_word:
                count+=len(word)

        return count
