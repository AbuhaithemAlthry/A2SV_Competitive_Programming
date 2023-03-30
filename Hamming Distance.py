class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return abs(x.bit_length()-y.bit_length())
