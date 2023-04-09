class Solution(object):
    def isToeplitzMatrix(self, matrix):
        dic = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in dic:
                    dic[r-c] = val
                elif dic[r-c] != val:
                    return False
        return True
