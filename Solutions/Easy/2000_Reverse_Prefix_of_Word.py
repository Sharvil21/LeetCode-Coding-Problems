#First Solution
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:]
        else:
            return word
#second Solution:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:] if ch in word else word
