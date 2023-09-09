class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        col = len(isWater)
        row = len(isWater[0])
        for i in range(col):
            for j in range(row):
                if isWater[i][j] == 1:
                    queue.append((i,j,0))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = [[float('inf') for i in range(row)] for j in range(col)]
        visited = set()
        while queue:
            y,x,height = queue.popleft()
            visited.add((y,x))
            ans[y][x] = min(ans[y][x],height)
            for dy,dx in directions:
                ny, nx = y+dy, x+dx
                if 0<=ny<col and 0<=nx<row and isWater[ny][nx] == 0 and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    queue.append((ny,nx,height+1))
        return ans