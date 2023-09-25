class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dfs(index,buy):
            if index >= len(prices):
                return 0
            
            if (index, buy) in memo:
                return memo[(index, buy)]
            
            res = 0
            if buy:
                yb = dfs(index+1, not buy)-prices[index]
                nb = dfs(index+1, buy)
                res = max(yb, nb)
            else:
                ys = dfs(index+1, not buy)+prices[index]-fee
                ns = dfs(index+1, buy)
                res = max(ys, ns)
            memo[(index,buy)] = res
            return res
        return dfs(0,True)
            