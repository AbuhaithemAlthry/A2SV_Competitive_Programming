class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(sum_, index):
            if (sum_,index) in memo:
                return memo[(sum_,index)]
            
            if index == len(nums) and sum_ == target:
                return 1

            if index >= len(nums):
                return 0 

            right = dfs(sum_ + nums[index], index + 1)

            left = dfs(sum_ - nums[index], index + 1)
            
            memo[(sum_,index)] = left + right

            return memo[(sum_,index)] 
    
        return dfs(0,0)