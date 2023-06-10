class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        n = len(nums)
        def helper(s,e):

            dp = [0]*(n)

            dp[s] =  nums[s]
            dp[s+1] = max(nums[s+1],nums[s])

            for i in range(2,e):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return max(dp)
        return max(helper(0,n-1),helper(1,n))