class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(picked, arr):
            if len(arr) == len(nums):
                result.append(arr)
            
			# picked is recording that the index that we picked. 
			
            for i in range(len(nums)):
			    # meaning we havent picked index i 
                if 1 << i & picked == 0:
                    dfs(picked | 1 << i , arr + [nums[i]])
        
        dfs(0, [])
        return result