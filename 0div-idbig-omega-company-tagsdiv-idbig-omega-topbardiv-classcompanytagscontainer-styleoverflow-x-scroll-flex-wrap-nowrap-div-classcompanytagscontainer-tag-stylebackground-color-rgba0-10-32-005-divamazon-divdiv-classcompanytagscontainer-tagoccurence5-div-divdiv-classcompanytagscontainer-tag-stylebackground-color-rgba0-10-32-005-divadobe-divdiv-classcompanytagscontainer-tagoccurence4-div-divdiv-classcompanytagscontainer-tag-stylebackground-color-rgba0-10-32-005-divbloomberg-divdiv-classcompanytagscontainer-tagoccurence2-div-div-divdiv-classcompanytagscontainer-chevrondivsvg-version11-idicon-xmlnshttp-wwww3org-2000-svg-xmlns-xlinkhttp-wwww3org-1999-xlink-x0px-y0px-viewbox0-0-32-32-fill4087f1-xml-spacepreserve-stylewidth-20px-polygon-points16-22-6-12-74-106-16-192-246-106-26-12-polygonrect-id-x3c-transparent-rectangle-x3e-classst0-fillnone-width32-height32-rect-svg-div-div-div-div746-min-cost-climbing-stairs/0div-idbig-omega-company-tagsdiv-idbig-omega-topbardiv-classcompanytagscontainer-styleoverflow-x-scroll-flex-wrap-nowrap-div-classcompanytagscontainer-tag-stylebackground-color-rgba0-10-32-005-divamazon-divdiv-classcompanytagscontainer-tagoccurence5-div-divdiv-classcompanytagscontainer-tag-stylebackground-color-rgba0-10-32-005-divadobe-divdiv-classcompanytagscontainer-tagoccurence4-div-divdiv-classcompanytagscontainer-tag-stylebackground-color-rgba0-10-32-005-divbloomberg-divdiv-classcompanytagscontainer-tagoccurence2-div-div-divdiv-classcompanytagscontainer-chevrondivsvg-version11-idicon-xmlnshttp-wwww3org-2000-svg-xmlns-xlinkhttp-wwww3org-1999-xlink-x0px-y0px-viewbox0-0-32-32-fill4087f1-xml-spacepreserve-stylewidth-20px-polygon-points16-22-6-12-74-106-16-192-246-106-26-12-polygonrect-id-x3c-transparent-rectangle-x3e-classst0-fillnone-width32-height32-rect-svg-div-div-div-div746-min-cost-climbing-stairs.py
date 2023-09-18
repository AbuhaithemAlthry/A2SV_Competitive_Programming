class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {  }

        def recursion(n):
            if n<2:
                return cost[n]
            if n in memo:
                return memo[n]
				
            result = min(recursion(n - 1), recursion(n - 2)) + cost[n]
            memo[n] = result
            return result

        cost.append(0)
        return recursion(len(cost)-1)
                