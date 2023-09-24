class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # Memoization dictionary

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')

            min_count = float('inf')
            for coin in coins:
                count = dfs(remain - coin)
                min_count = min(min_count, count + 1)

            memo[remain] = min_count
            return memo[remain]

        result = dfs(amount)
        return result if result != float('inf') else -1