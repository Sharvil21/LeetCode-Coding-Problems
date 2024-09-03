#First Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        for i in s.split():
            output = output + i[::-1] + ' '
        return output.strip()

#Second Solution
