class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        
        def dfs(remain):
            if remain==0:
                return 0
            if remain<0:
                return float('inf')
            s = float('inf')
            for coin in coins:
                s = min(s,dfs(remain-coin))
            return s + 1
        
        return dfs(amount) if dfs(amount)!=float('inf') else -1