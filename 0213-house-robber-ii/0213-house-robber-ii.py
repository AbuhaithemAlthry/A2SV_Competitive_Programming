class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top-down approach
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        memo = {}
        def dp(st, en):
            if en == st:
                return nums[en]
            if en == st + 1:
                return max(nums[st], nums[st + 1])
            if (st,en) not in memo:
                memo[(st,en)]=max(dp(st, en - 1), dp(st, en - 2) + nums[en])
            return memo[(st,en)]

        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))
        '''
        Bottom-up approach
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
        '''