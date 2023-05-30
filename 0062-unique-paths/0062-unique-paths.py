class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def backtrack(y,x):
            if (y==m) or (x==n):
                return 1
            if (y,x) in cache:
                return cache[(y,x)]
            cache[(y,x)] = backtrack(y+1,x) + backtrack(y,x+1)
            
            return cache[(y,x)]
        
        return backtrack(1,1)