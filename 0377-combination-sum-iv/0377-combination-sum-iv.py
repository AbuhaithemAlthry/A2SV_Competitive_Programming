class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        size = len(nums)
        memo = {}
        #TopDown approach
        def dfs(index, current_sum, target, nums, size, memo):
            if current_sum > target:
                return 0

            if (index,current_sum) in memo:
                return memo[(index,current_sum)]

            if current_sum == target:
                return 1

            answer = 0
            for i in range(size):
                answer += dfs(i, current_sum + nums[i], target, nums, size, memo)

            memo[(index,current_sum)] = answer
            return answer
        return dfs(0, 0, target, nums, size, memo)
    '''
    Bottomup approach
    def combinationSum4(self, N: List[int], T: int) -> int:
        dp = [0] * (T + 1)
        dp[0] = 1
        for i in range(T):
            if not dp[i]: continue
            for num in N:
                if num + i <= T: dp[i+num] += dp[i]

        return dp[T]
    '''