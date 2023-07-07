from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def isValid(row, col, val):
            if (0 <= row < len(matrix)) and (0 <= col < len(matrix[0])) and val < matrix[row][col]:
                return True
            return False

        def dfs(x, y):
            if memo[x][y] != 0:
                return memo[x][y]
            res = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isValid(nx, ny, matrix[x][y]):
                    res = max(res, 1 + dfs(nx, ny))
            memo[x][y] = res
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        return ans