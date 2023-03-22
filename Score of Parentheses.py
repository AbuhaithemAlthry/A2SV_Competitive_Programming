class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res,output = 0,0
        for i in s:
            if i == ")":
                s = stack.pop()
                
                if s == 0:
                    output = 1
                else:
                    output = (2*s)
                
                if not stack:
                    res += output
                else:
                    stack[-1] += output       
            else:
                stack.append(0)
        return res
