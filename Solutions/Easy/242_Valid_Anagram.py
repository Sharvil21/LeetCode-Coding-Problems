#first solution using collections.Counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
	return Counter(s) == Counter(t)

#2nd solution(Using sorted() function. But this increases time complexity)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

