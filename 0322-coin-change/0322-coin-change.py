class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remain):
            if remain==0:
                return 0
            if remain<0:
                return float('inf')
            s = float('inf')
            for child in coins:
                s = min(s,dfs(remain-child))
            return s + 1
        return dfs(amount) if dfs(amount)!=float('inf') else -1
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n=amount+1
#         dp = [float('inf')]*n
#         dp[0]=0
#         for i in range(1,n):
#             best = float('inf')
#             for coin in coins:
#                 if i-coin>=0:
#                     best = min(best,dp[i-coin])
#             dp[i] = best+1
#         return dp[-1] if dp[-1] != float('inf') else -1
            