class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(target):
            s = 0
            if target==0:
                return 1
            if target<0:
                return 0
            for child in nums:
                s += dfs(target-child)
            return s 
        
        return dfs(target)