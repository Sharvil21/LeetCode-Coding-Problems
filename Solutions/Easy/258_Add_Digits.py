class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            total = 0
            for i in list(str(num)):
                total += int(i)
            num = total
        return num
