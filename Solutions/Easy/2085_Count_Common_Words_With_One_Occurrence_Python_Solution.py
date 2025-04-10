#Python Solution using Counter
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        cnt = 0
        for i in counter1:
            if i in counter2:
                if counter1[i] == 1 and counter2[i] == 1:
                    cnt += 1

        return cnt


#Another Python Solution
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0

        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count=count+1

        return count
