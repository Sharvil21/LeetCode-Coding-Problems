#Python Solution using set
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for letter in s:
            if letter in seen:
                return letter
            else:
                seen.add(letter)

