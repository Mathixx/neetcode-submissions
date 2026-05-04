class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            if n & (1 << i):
                reverse |= (1 << (31-i))
        return reverse
                
        