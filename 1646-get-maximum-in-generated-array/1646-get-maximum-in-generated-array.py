class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        cache = {}

        def recurse(n):
            if n < 2:
                return n

            if n in cache:
                return cache[n]

            if n % 2 == 0:
                cache[n] = recurse(n // 2)
            else:
                cache[n] = recurse((n - 1) // 2) + recurse((n - 1) // 2 + 1)

            return cache[n]

        return max(recurse(i) for i in range(n + 1))