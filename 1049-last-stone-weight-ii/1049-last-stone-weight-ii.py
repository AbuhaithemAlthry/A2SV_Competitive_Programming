class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)
        # print(target)
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            take = dfs(i + 1, total + stones[i])
            dontTake = dfs(i + 1, total)
            
            dp[(i, total)] = min(take, dontTake)
            return dp[(i, total)]
        
        dp = {}
        return dfs(0, 0)