#First Solution: Create an empty dictionary, split the strings and get the count of each word in the dictionary. Then append only those words that have a value of 1 in an empty list. Beats 100%

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = {}
        op = []
        for i in s1.split():
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        for i in s2.split():
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        for word,count in ans.items():
            if count == 1:
                op.append(word)

        return op

#Modification of first solution
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = {}
        op = []
        for i in s1.split():
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        for i in s2.split():
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        for i in ans:
            if ans[i]==1:
                op.append(i)


        return op

