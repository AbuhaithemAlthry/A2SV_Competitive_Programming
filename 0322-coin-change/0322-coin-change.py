class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = {}
#         def count(remaining):
#             if remaining in memo:
#                 return memo[remaining]
#             best = float('inf')
#             if remaining<0:
#                 return float('inf')
#             if remaining==0:
#                 return 0

#             for coin in coins:
#                 best = min(best,count(remaining-coin))
#             memo[remaining] = best+1
#             return memo[remaining]

 
#         val = count(amount)

#         if val == float('inf'):
#             return -1
#         return val
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=amount+1
        dp = [float('inf')]*n
        dp[0]=0
        for i in range(1,n):
            best = float('inf')
            for coin in coins:
                if i-coin>=0:
                    best = min(best,dp[i-coin])
            dp[i] = best+1
        return dp[-1] if dp[-1] != float('inf') else -1
            