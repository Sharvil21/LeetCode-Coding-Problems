#First Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        for i in s.split():
            output = output + i[::-1] + ' '
        return output.strip()

#Second Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s,ans=list(s.split()),[]
        for i in s:
            ans.append(i[::-1])
        return ' '.join(ans)
