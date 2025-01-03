##Solution: Beats 100%. Use .insert() method to add a 'dummy' placeholder at index 0 in the list. Then use for loop, range(1,len(nums)):

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,'dummy')
        specials = []
        for i in range(1,len(nums)):
            if n%i == 0:
                specials.append(nums[i])

        return sum([i**2 for i in specials])

