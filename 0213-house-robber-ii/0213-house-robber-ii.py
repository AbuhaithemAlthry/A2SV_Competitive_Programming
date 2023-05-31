class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        def dp(start, end):
            if (start, end) not in memo:
                memo[start, end] = max(
                    nums[start] + (dp(start + 2, end) if start + 2 <= end else 0),
                    dp(start + 1, end) if start + 1 <= end else 0
                )
            return memo[start, end]

        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))