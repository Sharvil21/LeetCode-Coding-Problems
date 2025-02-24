#First Solution; Beats 66.64% currently
class Solution:
    def sortSentence(self, s: str) -> str:
        copy = s.split()[::-1]
        copy_2 = []
        for i in copy:
            copy_2.append(i[::-1])
        output = []

        for j in sorted(copy_2):
            output.append(j[1:][::-1])
        
        return ' '.join(output)

#Second Solution
class Solution:
    def sortSentence(self, s: str) -> str:
        new_arr = [i[::-1] for i in s.split()]
        new_arr.sort()
        output = ''
        for i in new_arr:
            output += ' ' + i[1:][::-1]
        return output.strip()

#Third Solution 
