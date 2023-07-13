class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        columns = [1] * col
        rows = [1] * row
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    columns[j] = 0
                    rows[i] = 0
                    
        for i in range(row):
            if not rows[i]:
                for j in range(col):
                    matrix[i][j] = 0

        for i in range(col):
            if not columns[i]:
                for j in range(row):
                    matrix[j][i] = 0