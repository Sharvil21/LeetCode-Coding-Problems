from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        count = Counter(nums)
        for i in nums:
            if count[i] == 1:
                output.append(i)
        return output

