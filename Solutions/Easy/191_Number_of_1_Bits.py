class Solution:
    def hammingWeight(self, n: int) -> int:
        notation = bin(n)[2:]
        total_bits = 0
        for i in notation:
            if i == '1':
                total_bits += 1

        return total_bits
        
