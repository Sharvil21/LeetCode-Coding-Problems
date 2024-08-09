class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                output += 1
        return output
