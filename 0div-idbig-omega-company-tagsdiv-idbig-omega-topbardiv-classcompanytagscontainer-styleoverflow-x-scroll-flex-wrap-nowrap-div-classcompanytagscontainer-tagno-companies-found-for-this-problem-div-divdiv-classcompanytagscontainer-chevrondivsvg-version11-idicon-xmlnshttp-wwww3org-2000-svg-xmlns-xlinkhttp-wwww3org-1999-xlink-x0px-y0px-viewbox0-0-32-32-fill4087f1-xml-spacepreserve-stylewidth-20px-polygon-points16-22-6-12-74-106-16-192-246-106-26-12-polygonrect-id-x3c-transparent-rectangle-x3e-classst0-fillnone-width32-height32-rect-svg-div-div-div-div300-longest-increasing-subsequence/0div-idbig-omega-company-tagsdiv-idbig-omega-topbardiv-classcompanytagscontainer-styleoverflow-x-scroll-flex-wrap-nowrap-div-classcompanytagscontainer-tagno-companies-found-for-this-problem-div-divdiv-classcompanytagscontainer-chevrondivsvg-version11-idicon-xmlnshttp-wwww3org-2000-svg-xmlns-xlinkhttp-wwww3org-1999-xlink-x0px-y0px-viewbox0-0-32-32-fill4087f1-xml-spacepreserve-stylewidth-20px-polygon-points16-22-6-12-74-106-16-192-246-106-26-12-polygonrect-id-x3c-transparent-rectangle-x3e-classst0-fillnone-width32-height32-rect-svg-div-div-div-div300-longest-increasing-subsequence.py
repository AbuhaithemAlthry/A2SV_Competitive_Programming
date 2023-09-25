class Solution:
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[[0 for j in range(n+1)] for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1): #it will go to -1 but since we are doing "+1" at prev index so it will go up to 0
                not_take=0+dp[ind+1][prev+1]
                take=0
                if prev==-1 or nums[ind]>nums[prev]:
                    take=1+dp[ind+1][ind+1]
                dp[ind][prev+1]=max(take,not_take)
        return dp[0][0]