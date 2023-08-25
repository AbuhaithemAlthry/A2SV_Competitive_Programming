class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(i,j):
            if i >= len(grid) or i < 0 or 0 > j or j >=len(grid[0]) or grid[i][j]=='0':
                return 
            
            visited.add((i,j))
            for dx,dy in directions:
                if (i+dx,j+dy) not in visited:
                    dfs(i+dx,j+dy)
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    dfs(i,j)
                    count+=1      
        return count