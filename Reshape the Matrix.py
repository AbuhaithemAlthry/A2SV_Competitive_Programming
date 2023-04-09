class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat or r*c != len(mat) * len(mat[0]):
            return mat
     
        l = [[0 for _ in range(c)] for _ in range(r)]
        print(l)

        n=len(mat[0])

        i=0
        while i < r*c:
            l[i//c][i%c] = mat[i//n][i%n]  
            i+=1
        return l
