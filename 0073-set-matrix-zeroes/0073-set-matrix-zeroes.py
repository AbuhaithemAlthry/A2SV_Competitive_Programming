class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = len(matrix)
        row = len(matrix[0])
        matrix_copy = copy.deepcopy(matrix)
        print(matrix_copy)
        for i in range(col):
            for j in range(row):
                if matrix_copy[i][j] == 0:
                    for y in range(row):
                        matrix[i][y] = 0

                    for x in range(col):
                        matrix[x][j] = 0
                        