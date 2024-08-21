#First Solution: Using Counter() Function
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i in s:
            if count[i] == 1:
                return s.index(i)
        return -1

#Second Solution: Create a empty dictionary. Add the count of each character. Iterate through the dictionary and return the first character that has count = 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #2nd solution using dictionary
        empty_dict = {}
        for i in s:
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
        
        for i in s:
            if empty_dict[i] == 1:
                return s.index(i)
        return -1
                                
