#Used set() function along with sorted. Make a set of the list of numbers. Then sort it. If the length is less than 3, return the last number in that array/list/set. Else return the last third number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        var = sorted(set(nums))
        if len(var) <3:
            return var[-1]
        else:
            return var[-3]
