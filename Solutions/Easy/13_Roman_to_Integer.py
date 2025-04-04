class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        i = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while i < len(s):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                number = number + roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                number = number + roman[s[i]]
                i += 1
        return number
