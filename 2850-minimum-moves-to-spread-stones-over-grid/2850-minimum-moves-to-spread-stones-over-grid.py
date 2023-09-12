class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.min_step = float('inf')
        
        stoneiszero = []
        stonelt1 = set()

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    stoneiszero.append((i,j))
                elif grid[i][j] > 1:
                    stonelt1.add((i,j))
        
        def dfs(step):
            if len(stonelt1) == 0:
                self.min_step = min(step, self.min_step)
                return
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        for xi, xj in stonelt1:
                            grid[i][j] = 1
                            grid[xi][xj] -=1
                            stonelt1.remove((xi, xj))
                            if grid[xi][xj] >= 2:
                                stonelt1.add((xi,xj))
                                
                            dfs(step + abs(xi-i) + abs(xj-j))
                            
                            grid[i][j] = 0
                            grid[xi][xj] +=1
                            stonelt1.add((xi,xj))
            return 
        dfs(0)
        return self.min_step