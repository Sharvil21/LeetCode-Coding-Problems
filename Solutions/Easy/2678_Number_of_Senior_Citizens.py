#Solution that beats 100%
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = []
        count = 0
        for i in details:
            ages.append(i[11:13])

        for i in ages:
            if int(i)> 60:
                count+=1

        return count

#Second Solution - A bit concise code. Almost same time complexity:

class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        counter = 0
        for i in details:
            if int(i[11:13]) > 60:
                counter+=1
        return counter
