class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        y = num**0.5

        return y.is_integer()
