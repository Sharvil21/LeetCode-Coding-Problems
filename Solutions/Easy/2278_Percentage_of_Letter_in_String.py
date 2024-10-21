#Python Solution using floor division
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in s:
            if i == letter:
                count += 1

        return 100*count//len(s)
