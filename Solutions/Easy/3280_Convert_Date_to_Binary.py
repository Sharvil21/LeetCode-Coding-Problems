#
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        binary_notation = ''
        for i in date.split('-'):
            bin_number = bin(int(i))
            binary_notation += bin_number[2:] + '-'

        return binary_notation[:-1]
