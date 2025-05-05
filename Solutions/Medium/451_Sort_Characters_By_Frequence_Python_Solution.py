#Python Solution
#Will have to use the Counter library from collections
#Create a dictionary first using Counter.
#The logic is to sort the Counter dictionary using the frequency of the keys in descending order. We can use the sorted() function for this. But We'll also have to use a lambda function
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        lst = []
        for key, value in sorted(Counter(s).items(), key = lambda x: x[1], reverse = True):
            lst.append(key*value)
        return "".join(lst)

