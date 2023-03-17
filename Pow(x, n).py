class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(k, n):
            if k == 0: 
                return 0
            if n == 0:
                return 1
            print(n)
            res = helper(k, n//2)
            res = res * res
            return res * k if n%2 == 1 else res
        a = helper(x,abs(n))
        return a if n>=0 else 1/a
