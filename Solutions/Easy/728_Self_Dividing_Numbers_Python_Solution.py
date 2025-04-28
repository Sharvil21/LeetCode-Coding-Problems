#Python Solution
#Have to use for loops and iterations to check the condition
#Create an empty list first
#Then iterate a for loop in the range specified
#Then for each iteration, convert it to a string, and run a for loop for each value in the string.
#If the value is 0 or the modulus isn't 0, then break the loop.
#else, append the value into the list
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        op = []
        for num in range(left,right+1):
            valid = True
            for digit in str(num):
                if int(digit) == 0 or num%int(digit) != 0 :
                    valid = False
                    break
            if valid:
                op.append(num)
        return op
