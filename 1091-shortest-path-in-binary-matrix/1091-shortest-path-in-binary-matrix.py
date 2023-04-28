class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        rows,cols = len(grid),len(grid[0])
        
        level = 1
        levels = deque([(0,0,level)])
        visited = set([(0,0)])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
        while levels:
            row, col, dist = levels.popleft()
            if row == rows-1 and col == cols-1:
                return dist
            
            for r, c in directions:
                nr = row + r 
                nc = col + c
                if rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr,nc))
                    levels.append((nr, nc, dist + 1))
        return -1
    
