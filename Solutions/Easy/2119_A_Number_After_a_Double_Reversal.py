#First solution
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num%10 != 0 or num == 0:
            return (str(num)[::-1])[::-1] == str(num)
        else:
            return False
    

#Second Solution: 1 Liner 
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return (num==0) or (num%10!=0)
            
