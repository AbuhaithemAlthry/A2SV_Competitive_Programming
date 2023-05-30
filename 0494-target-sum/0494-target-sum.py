class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}

        def backtrack(index,total):
            if index == len(nums):
                return 1 if total == target else 0
            
            if (index,total) in cache:
                return cache[(index,total)]
            
            cache[(index,total)] = backtrack(index+1,total+nums[index]) + backtrack(index+1,total-nums[index])
            return cache[(index,total)]
        
        return backtrack(0,0)