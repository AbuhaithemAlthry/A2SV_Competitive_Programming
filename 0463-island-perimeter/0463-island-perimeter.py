class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or  j < 0 or j >= len(grid[0]) or grid[i][j]==0:
                return 1
            
            perimeter = 0
            
            if (i, j) not in vis:
                vis.add((i,j))
                perimeter += dfs(i+1,j)
                perimeter += dfs(i,j+1)
                perimeter += dfs(i-1,j)
                perimeter += dfs(i,j-1)
            
            return perimeter
            
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)