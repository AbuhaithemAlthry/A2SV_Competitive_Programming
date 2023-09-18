class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rec(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0],nums[1])
            if i not in memo:
                memo[i] = max(rec(i - 1), rec(i - 2) + nums[i])
            return memo[i]
        return rec(len(nums)-1)
        