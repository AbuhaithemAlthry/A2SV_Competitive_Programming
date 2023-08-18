class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        valid = [['.'] * n for _ in range(n)]
        posDiagonal = set()
        negDiagonal = set()
        column = set()
        res = []

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in valid])
                return
            for c in range(n):
                if c in column or r+c in posDiagonal or r-c in negDiagonal:
                    continue
                    
                column.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                valid[r][c] = 'Q'

                backtrack(r+1)

                column.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                valid[r][c] = '.'
        backtrack(0)
        return res