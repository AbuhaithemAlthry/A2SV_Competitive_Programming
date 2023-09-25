class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        memo = {}
        def dfs(op,j,total):
            if (op,j,total) in memo:
                return memo[(op,j,total)]
            if total == n:
                return 0
            if total > n:
                return float('inf')
            result = float('inf')
            if op == 'p':
                memo[(op,j,total)] = min(1+dfs('p',j,total+j),1+dfs('c',total,total))
                return memo[(op,j,total)]
            if op == 'c':
                memo[(op,j,total)] = 1 + dfs('p',j,total+j)
                return memo[(op,j,total)]
            
        return 1 + dfs('p',1,1)