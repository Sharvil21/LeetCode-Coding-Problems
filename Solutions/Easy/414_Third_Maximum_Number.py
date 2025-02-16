class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        var = sorted(set(nums))
        if len(var) <3:
            return var[-1]
        else:
            return var[-3]
