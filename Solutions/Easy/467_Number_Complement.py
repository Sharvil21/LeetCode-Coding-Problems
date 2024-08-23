class Solution:
    def findComplement(self, num: int) -> int:
        original_binary_number = bin(num)[2:]
        complement_number = []
        for i in original_binary_number:
            if i == '0':
                complement_number.append('1')
            else:
                complement_number.append('0')

        return int(''.join(complement_number),2)
            
