class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        for i in range(n.bit_length() - 1, 0, -1):
            current_bit = (n & (1 << i)) >> i
            previous_bit = (n & (1 << (i - 1))) >> (i - 1)
            if current_bit == previous_bit:
                return False
        return True