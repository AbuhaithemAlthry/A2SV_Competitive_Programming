class Solution:
    memo = defaultdict(int)
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n<3:
            return 1
        if self.memo[n]:
            return self.memo[n]
        
        self.memo[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        
        return self.memo[n]