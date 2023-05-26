class Solution:
    memo = defaultdict(int)
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        if self.memo[n]:
            return self.memo[n]
        self.memo[n] = self.fib(n-1)+self.fib(n-2)
        return self.fib(n-1)+self.fib(n-2)
        