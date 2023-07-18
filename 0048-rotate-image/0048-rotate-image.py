class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r= 0,len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                
                top_left = matrix[top+i][l]
                
                matrix[top+i][l] = matrix[bottom][l+i]
                
                matrix[bottom][l+i] = matrix[bottom-i][r]
                
                matrix[bottom-i][r] = matrix[top][r-i]
                
                matrix[top][r-i] = top_left
            l+=1
            r-=1