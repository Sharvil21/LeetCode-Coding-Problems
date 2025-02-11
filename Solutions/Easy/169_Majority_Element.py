#1st solution which leads to timeout error. But it still works with the testcases ( most of em)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if n == 1:
                return nums[i]
            word_count = 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    word_count += 1
                    if word_count > n/2:
                        return nums[i]

#2nd solution:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
