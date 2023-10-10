class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}
        def dp(index, time):
            if (index, time) in memo:
                return memo[(index, time)]
            if index > len(satisfaction) - 1:
                return 0
            memo[(index, time)] = max(satisfaction[index] * time + dp(index + 1, time + 1), dp(index + 1, time))
            return memo[(index, time)]
        
        return dp(0, 1)