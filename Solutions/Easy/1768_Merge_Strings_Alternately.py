class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        for i in list(zip(word1,word2)):
            for j in i:
                output += j

        if len(word1) < len(word2):
            output = output + word2[len(word1):]
        elif len(word2) < len(word1):
            output = output + word1[len(word2):]
        return output

#2nd solution:
def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        st = ""
        for i in range(n):
            st += word1[i]+word2[i]
        return st+word1[n:]+word2[n:]
