#Python Solution using for loop
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                added_num = num[i] + num[i+1] + num[i+2]
                nums.append((added_num))
        if len(nums) == 0:
            return ""
        else:
            return str(max(nums))
