class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        top-down
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0],nums[1])
            return max(dp(i - 1), dp(i - 2) + nums[i])
        return dp(len(nums)-1)
        '''
        #bottom-up
        n = len(nums)

        if n==1:
            return nums[0]
        
        dp = [0]*(n)
        
        dp[0] =  nums[0]
        dp[1] = max(nums[1],nums[0])
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
        return dp[-1]