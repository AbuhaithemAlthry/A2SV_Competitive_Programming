class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        answer = 1
        for a in arr:
            before_a = dp[a - difference]
            dp[a] = before_a + 1
            answer = max(answer, dp[a])
            
        return answer