# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         cache = {}
#         def backtrack(y,x):
#             if (y==m) or (x==n):
#                 return 1
#             if (y,x) in cache:
#                 return cache[(y,x)]
#             cache[(y,x)] = backtrack(y+1,x) + backtrack(y,x+1)
            
#             return cache[(y,x)]
        
#         return backtrack(1,1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        matrix = []
        for i in range(m):
            matrix.append(row)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                matrix[i][j]=matrix[i+1][j]+matrix[i][j+1]
        return matrix[0][0]