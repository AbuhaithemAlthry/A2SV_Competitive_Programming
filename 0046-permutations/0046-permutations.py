class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = [0] * n

        def backtrack(permutation):
            if len(permutation) == n:
                result.append(permutation[:])
                return 

            for i in range(n):
                if visited[i] == 0:
                    visited[i] = 1
                    permutation.append(nums[i])
                    backtrack(permutation)
                    visited[i] = 0
                    permutation.pop()

        backtrack([])
        return result