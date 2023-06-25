class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i == len(s): 
                return 1
            ans = 0
            if i not in memo:
                if s[i] != '0':  # Single digit
                    ans += dp(i + 1)
                if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):  # Two digits
                    ans += dp(i + 2)
                memo[i]=ans
            return memo[i]
        return dp(0)