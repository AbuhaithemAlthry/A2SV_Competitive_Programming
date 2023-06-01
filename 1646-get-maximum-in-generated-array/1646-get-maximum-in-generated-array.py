class Solution:
#    using top-down
#     def getMaximumGenerated(self, n: int) -> int:
#         cache = {}

#         def recurse(n):
#             if n < 2:
#                 return n

#             if n in cache:
#                 return cache[n]

#             if n % 2 == 0:
#                 cache[n] = recurse(n // 2)
#             else:
#                 cache[n] = recurse((n - 1) // 2) + recurse((n - 1) // 2 + 1)

#             return cache[n]

#         return max(recurse(i) for i in range(n + 1))

#   using bottom-up
    def getMaximumGenerated(self, n: int) -> int:
        if n<2:
            return n
        dp = [0]*(n+1)
        dp[0],dp[1] = 0,1
        for i in range(2,n+1):
            if i%2==0:
                dp[i] = dp[i//2] 
            else:
                dp[i] = dp[(i-1)//2] + dp[(i-1)//2 +1]
        return max(dp)
        
        