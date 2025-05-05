#Python Solution
#Used Counter from collections library
#Create a counter of the numbers in the list
#Iterate through it, then add only the unique elements in a different list
#Lastly, return the sum of that new list
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_elements = []
        for num, total in count.items():
            if total == 1:
                unique_elements.append(num)
        return sum(unique_elements)


