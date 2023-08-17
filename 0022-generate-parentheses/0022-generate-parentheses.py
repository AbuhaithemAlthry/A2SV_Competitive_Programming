class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtracking(op,cl,cur):
            if op==cl==n:
                res.append(''.join(cur[:]))
                # return
            if op < n:
                cur.append('(')
                backtracking(op+1,cl,cur)
                cur.pop()
            if cl < op:
                cur.append(')')
                backtracking(op,cl+1,cur)
                cur.pop()
                
        backtracking(0,0,[])
        return res
            