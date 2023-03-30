class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(31,-1,-1):
            if (x & (1 << i)) != (y & (1 << i)) :
                count+=1
        return count
