class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        var = ''.join(list(map(str,nums)))
        digit_sum = 0
        element_sum = sum(nums)

        for i in var:
            digit_sum += int(i)
        
        return abs(element_sum - digit_sum)

