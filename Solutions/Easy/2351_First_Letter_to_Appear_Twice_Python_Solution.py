#Python Solution using set
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for letter in s:
            if letter in seen:
                return letter
            else:
                seen.add(letter)

#Another Python Solution using list
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = []
        for letter in s:
            if letter in l:
                return letter
            else:
                l.append(letter)

