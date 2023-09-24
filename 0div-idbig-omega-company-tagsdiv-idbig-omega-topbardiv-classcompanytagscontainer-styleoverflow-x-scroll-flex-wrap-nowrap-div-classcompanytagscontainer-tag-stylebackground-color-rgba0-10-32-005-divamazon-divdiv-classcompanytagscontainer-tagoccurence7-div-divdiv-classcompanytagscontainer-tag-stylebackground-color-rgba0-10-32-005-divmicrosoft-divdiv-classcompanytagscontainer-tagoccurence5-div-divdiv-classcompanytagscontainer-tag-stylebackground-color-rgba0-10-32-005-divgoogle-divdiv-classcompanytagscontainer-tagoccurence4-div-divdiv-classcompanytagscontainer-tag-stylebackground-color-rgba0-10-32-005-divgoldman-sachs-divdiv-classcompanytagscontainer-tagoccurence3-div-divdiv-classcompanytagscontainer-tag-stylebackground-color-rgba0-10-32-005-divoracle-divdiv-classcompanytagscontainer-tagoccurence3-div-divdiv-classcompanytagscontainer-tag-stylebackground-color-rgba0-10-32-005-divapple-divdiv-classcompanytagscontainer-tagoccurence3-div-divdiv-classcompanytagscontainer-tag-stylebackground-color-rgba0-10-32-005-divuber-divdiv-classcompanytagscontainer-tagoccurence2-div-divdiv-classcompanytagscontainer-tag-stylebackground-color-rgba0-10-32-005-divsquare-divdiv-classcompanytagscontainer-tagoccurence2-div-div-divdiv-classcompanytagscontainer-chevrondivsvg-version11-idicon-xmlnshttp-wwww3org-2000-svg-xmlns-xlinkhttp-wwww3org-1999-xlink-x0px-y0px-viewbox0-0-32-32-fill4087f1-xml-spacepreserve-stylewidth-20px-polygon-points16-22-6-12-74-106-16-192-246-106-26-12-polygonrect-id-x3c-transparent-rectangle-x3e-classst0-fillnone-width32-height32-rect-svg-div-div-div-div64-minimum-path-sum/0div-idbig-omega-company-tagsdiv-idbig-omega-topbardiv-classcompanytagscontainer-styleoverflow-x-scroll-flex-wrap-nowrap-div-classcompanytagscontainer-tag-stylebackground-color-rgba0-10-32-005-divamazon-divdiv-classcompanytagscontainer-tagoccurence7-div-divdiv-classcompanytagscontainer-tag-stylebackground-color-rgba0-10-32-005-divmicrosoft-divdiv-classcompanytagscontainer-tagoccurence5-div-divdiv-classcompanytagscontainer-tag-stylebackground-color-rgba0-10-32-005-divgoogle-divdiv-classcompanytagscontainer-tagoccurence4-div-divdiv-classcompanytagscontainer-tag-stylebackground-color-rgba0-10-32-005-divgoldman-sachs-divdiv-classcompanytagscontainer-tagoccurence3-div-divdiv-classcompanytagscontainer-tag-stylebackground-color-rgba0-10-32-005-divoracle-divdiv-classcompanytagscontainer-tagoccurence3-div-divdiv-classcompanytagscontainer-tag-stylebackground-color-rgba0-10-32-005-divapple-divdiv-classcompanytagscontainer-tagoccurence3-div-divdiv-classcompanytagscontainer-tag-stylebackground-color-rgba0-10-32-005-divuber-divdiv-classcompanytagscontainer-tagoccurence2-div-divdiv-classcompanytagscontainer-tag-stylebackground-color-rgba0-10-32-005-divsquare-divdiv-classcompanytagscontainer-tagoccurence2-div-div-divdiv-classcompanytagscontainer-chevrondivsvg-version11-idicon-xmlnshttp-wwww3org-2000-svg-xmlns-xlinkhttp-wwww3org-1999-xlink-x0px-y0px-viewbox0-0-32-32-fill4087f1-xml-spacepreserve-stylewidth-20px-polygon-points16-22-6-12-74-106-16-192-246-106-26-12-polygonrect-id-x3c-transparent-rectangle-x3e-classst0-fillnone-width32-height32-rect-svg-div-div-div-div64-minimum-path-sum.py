class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cache = {}
        def dp(i, j):
            if i >= m or j>=n:
                return float('inf')
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            
			# return from cache if present
            if (i,j) in cache :
                return cache[(i,j)]
			
			# populate cache
            cache[(i,j)] = grid[i][j] + min(dp(i+1,j), dp(i,j+1))
            return cache[(i,j)]
            

        return dp(0, 0)