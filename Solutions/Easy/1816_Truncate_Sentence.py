#Using .split() method along with slicing and .join method
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


#Attempting again. Came up with the same solution
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])

#The idea is to first use .split() method to split the sentence in a list
#Then use indexing to get only the words till the value 'k'.
#And then lastly use " ".join() method to turn the list into a sentence and return it
