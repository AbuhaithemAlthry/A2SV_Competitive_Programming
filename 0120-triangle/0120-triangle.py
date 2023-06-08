class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache  = {}
        def dfs(i, j):
            if i == len(triangle):
                return 0
            if (i,j) not in cache:
                lower_left = triangle[i][j] + dfs(i + 1, j)
                lower_right = triangle[i][j] + dfs(i + 1, j + 1)
                cache[(i,j)] = min(lower_left, lower_right)

            return cache[(i,j)]

        return dfs(0, 0)
            