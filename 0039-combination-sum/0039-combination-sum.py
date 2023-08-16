class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i,arr,tot):
            if tot == target:
                res.append(arr[:])
                return
            if i >= len(candidates) or tot > target:
                return
            
            arr.append(candidates[i])
            backtrack(i,arr,tot+candidates[i])
            arr.pop()
            backtrack(i+1,arr,tot)
        
        backtrack(0,[],0)
        return res