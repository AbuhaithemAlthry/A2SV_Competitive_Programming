class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        print(digits[0])
        def backtracking(i,cur):
            if i >= len(digits):
                res.append(''.join(cur[:]))
                return
            for child in dic[digits[i]]:
                cur.append(child)
                backtracking(i+1,cur)
                cur.pop()

        backtracking(0,[])
        return res
            