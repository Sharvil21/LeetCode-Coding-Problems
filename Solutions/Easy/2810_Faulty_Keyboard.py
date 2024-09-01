#First solution: Beats around 38%
class Solution:
    def finalString(self, s: str) -> str:
        word = []
        for i in s:
            if i != 'i':
                word.append(i)
            else:
                word = word[::-1]
        return ''.join(word)
