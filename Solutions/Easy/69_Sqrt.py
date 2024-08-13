#Cannot use any function or num**05 for this question
#Best option is to use Newton's Method for Integer to find the square root

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return int(r)
