class Solution:
    def findComplement(self, num: int) -> int:
        bi = list(bin(num)[2:])

        for i in range(num.bit_length()):
            if int(bi[i]):
                bi[i] = "0"
            else:
                bi[i] = "1"

        bi = "".join(bi)
        return int(bi,2)
