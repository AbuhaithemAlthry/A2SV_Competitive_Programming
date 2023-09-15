class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    min_sum[i][j] = grid[i][j]
                elif i == 0:
                    min_sum[i][j] = min_sum[i][j-1] + grid[i][j]
                elif j == 0:
                    min_sum[i][j] = min_sum[i-1][j] + grid[i][j]
                else:
                    min_sum[i][j] = min(min_sum[i][j-1], min_sum[i-1][j]) + grid[i][j]
        
        return min_sum[-1][-1]