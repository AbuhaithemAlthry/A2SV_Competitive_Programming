class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trs_matrix=[]
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            trs_matrix.append(tmp)
            tmp = []   
        return trs_matrix