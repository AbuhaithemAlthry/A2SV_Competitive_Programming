class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            bit = 1 << i
            for num in nums:
                if num & bit:
                    count += 1
            if count % 3:
                result |= bit
        return result if result < 2**31 else result - 2**32