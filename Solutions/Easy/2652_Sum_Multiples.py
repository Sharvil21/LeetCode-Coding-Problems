class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1,n+1):
            if i%7 == 0 or i %3 == 0 or i%5 == 0:
                total += i
        return total
