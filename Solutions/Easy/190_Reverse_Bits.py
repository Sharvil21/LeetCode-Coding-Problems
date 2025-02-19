class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = int(bin(n)[2:].zfill(32)[::-1],2)
        return reversed

            
