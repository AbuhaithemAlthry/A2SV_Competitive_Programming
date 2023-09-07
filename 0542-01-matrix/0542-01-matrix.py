class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    q.append((row, col, 0))
                    visited.add((row, col))
        res = [[0 if mat[row][col] == 0 else float('inf') for col in range(COLS)] for row in range(ROWS)]
        while q:
            row, col, distance = q.popleft()
            res[row][col] = min(res[row][col], distance)
            
            for dRow, dCol in directions:
                newRow, newCol = row + dRow, col + dCol
                if (0 <= newRow < ROWS and
                    0 <= newCol < COLS and
                    (newRow, newCol) not in visited and
                    mat[newRow][newCol] == 1):
                    q.append((newRow, newCol, distance + 1))
                    visited.add((newRow, newCol))
        return res