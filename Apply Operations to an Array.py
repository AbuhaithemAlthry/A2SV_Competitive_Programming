class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1], nums[i] = 2 * nums[i], 0

        i = 0
        for j, n in enumerate(nums):
            if n:
                nums[i], nums[j] = n, nums[i]
                i += 1

        return nums
