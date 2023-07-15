class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        n = len(digits)
        res = []
        dictionary = {
              "2":["a","b","c"],
              "3":["d","e","f"],
              "4":["g","h","i"],
              "5":["j","k","l"],
              "6":["m","n","o"],
              "7":["p","q","r","s"],
              "8":["t","u","v"],
              "9":["w","x","y","z"]
        }
        
        def backtrack(res,subset, index,digits):
            if len(digits) == index:
                res.append(''.join(subset))
                return 
            for i in dictionary[digits[index]]:
                subset.append(i)
                backtrack(res,subset,index+1,digits)
                subset.pop()

        backtrack(res,[],0,digits)
        return res