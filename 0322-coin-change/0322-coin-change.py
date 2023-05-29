class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def count(remaining):
            if remaining in memo:
                return memo[remaining]
            best = float('inf')
            if remaining<0:
                return float('inf')
            if remaining==0:
                return 0

            for coin in coins:
                best = min(best,count(remaining-coin)+1)
            memo[remaining] = best
            return best

 
        val = count(amount)

        if val == float('inf'):
            return -1
        return val