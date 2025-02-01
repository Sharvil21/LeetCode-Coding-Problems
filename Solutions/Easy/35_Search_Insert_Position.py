class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
                break
            elif target > nums[-1]:
                return len(nums)
                break
            elif nums[i] < target:
                if target < nums[i+1]:
                    return i+1
                    break
            elif target < nums[i]:
                return i
                break
            elif target > nums[i]:
                return i+1
                break
