class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        col = len(grid)
        row = len(grid[0])
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 1:
                    queue.append((i,j,0))

        if not queue or len(queue) == col*row:
            return -1
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_ = 0
        while queue:
            y , x , distance = queue.popleft()
            max_ = max(max_,distance)
            visited.add((y,x))
            for dy , dx in directions:
                ny , nx = y + dy , x + dx 
                if 0 <= ny < col and 0 <= nx < row and grid[ny][nx] == 0 and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    queue.append((ny,nx,distance+1))

        return max_