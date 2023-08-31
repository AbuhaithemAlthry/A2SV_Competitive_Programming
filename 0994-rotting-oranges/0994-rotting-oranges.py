class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        queue = deque()
        row, col = len(grid), len(grid[0])  # Corrected the range calculation
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):  # Use _ as a throwaway variable for the loop
                ory, orx = queue.popleft()
                for dy, dx in directions:
                    y = ory + dy
                    x = orx + dx
                    if 0 <= y < row and 0 <= x < col and grid[y][x] == 1:
                        grid[y][x] = 2
                        queue.append([y, x])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
            