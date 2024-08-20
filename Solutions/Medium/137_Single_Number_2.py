from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i
        
