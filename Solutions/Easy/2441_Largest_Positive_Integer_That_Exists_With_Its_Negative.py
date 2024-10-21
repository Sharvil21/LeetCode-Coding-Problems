#Brute Force Solution
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largest = -1
        for i in sorted(nums):
            if -i in nums:
                largest = i
        return largest
