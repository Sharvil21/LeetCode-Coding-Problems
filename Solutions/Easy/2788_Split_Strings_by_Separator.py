#Python Solutioin
class Solution:
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for i in word.split(separator):
                if i:
                    ans.append(i)
        return ans

#Another Python Solutioni using List Comprehension
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [i for word in words for i in word.split(separator) if i]
