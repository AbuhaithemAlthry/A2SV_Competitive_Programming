class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(i: int, j: int, player: int, total1: int, total2: int) -> bool:
            if i > j:
                if player == 1:
                    return total1 >= total2
                else:
                    return total2 > total1
            if player == 1:
                return not dfs(i + 1, j, 2, total1 + nums[i], total2) or not dfs(i, j - 1, 2, total1 + nums[j], total2)
            else:
                return not dfs(i + 1, j, 1, total1, total2 + nums[i]) or not dfs(i, j - 1, 1, total1, total2 + nums[j])
        
        n = len(nums)
        return dfs(0, n - 1, 1, 0, 0)