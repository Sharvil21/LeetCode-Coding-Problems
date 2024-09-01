#First Solution:
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []
        num2 = []
        for i in range(1,n+1):
            if i%m != 0:
                num1.append(i)
            if i%m == 0:
                num2.append(i)
        return sum(num1) - sum(num2)

#Second Solution
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if i%m != 0:
                num1 += i
            elif i%m == 0 :
                num2 += i
        
        return num1-num2
