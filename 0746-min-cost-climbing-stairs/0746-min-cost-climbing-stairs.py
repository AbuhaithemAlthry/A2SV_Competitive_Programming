class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         memo = {  }

#         def recursion(n):
#             if n<2:
#                 return cost[n]
#             if n in memo:
#                 return memo[n]
				
#             result = min(recursion(n - 1), recursion(n - 2)) + cost[n]
#             memo[n] = result
#             return result

#         cost.append(0)
#         return recursion(len(cost)-1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        dp = [0]*n
        dp[0],dp[1] = cost[0],cost[1]
        cost.append(0)
        for i in range(2,n):
            dp[i] = min(dp[i-1],dp[i-2])+cost[i]
        return dp[-1]