class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_rev = set()
        for num in nums:
            nums_rev.add(num)
            nums_rev.add(int(str(num)[::-1]))
        return len(nums_rev)