#Solution
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = len(text.split())
        for word in text.split():
            for j in brokenLetters:
                if j in word:
                    count -= 1
                    break
        return count
