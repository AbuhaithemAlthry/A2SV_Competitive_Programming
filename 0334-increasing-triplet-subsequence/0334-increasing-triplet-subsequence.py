class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small = float('inf')
        second_small = float('inf')
        for i in nums:
            if i>second_small:
                return True
            if i<first_small:
                first_small=i
            elif i>first_small:
                second_small=i
        return False