class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper, down = -1, len(matrix)
        while down > upper+1:
            mid = (upper + down) // 2
            if matrix[mid][0] <= target <=matrix[mid][len(matrix[mid])-1]:
                break
            elif matrix[mid][0] < target:
                upper = mid 
            else:
                down = mid 

        row = mid
        left,right = -1,len(matrix[row])

        while right > left + 1:
            mid = (left + right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        return False
