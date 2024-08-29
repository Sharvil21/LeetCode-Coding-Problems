#First solution: Very long time complexity. Almost at the highest in Leetcode:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count:
            if count[i] >2:
                while count[i] > 2:
                    j = nums.index(i)
                    nums.pop(j)
                    count = Counter(nums)

        return len(nums)
