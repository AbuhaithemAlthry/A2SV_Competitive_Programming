class Solution:
    memo =defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        if self.memo[n]:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.climbStairs(n-1)+self.climbStairs(n-2)