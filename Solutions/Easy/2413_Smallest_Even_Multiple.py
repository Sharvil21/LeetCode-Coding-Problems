class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,n+1):
            if n%2 == 0 and n%i == 0:
                return n
        
        return n*2


