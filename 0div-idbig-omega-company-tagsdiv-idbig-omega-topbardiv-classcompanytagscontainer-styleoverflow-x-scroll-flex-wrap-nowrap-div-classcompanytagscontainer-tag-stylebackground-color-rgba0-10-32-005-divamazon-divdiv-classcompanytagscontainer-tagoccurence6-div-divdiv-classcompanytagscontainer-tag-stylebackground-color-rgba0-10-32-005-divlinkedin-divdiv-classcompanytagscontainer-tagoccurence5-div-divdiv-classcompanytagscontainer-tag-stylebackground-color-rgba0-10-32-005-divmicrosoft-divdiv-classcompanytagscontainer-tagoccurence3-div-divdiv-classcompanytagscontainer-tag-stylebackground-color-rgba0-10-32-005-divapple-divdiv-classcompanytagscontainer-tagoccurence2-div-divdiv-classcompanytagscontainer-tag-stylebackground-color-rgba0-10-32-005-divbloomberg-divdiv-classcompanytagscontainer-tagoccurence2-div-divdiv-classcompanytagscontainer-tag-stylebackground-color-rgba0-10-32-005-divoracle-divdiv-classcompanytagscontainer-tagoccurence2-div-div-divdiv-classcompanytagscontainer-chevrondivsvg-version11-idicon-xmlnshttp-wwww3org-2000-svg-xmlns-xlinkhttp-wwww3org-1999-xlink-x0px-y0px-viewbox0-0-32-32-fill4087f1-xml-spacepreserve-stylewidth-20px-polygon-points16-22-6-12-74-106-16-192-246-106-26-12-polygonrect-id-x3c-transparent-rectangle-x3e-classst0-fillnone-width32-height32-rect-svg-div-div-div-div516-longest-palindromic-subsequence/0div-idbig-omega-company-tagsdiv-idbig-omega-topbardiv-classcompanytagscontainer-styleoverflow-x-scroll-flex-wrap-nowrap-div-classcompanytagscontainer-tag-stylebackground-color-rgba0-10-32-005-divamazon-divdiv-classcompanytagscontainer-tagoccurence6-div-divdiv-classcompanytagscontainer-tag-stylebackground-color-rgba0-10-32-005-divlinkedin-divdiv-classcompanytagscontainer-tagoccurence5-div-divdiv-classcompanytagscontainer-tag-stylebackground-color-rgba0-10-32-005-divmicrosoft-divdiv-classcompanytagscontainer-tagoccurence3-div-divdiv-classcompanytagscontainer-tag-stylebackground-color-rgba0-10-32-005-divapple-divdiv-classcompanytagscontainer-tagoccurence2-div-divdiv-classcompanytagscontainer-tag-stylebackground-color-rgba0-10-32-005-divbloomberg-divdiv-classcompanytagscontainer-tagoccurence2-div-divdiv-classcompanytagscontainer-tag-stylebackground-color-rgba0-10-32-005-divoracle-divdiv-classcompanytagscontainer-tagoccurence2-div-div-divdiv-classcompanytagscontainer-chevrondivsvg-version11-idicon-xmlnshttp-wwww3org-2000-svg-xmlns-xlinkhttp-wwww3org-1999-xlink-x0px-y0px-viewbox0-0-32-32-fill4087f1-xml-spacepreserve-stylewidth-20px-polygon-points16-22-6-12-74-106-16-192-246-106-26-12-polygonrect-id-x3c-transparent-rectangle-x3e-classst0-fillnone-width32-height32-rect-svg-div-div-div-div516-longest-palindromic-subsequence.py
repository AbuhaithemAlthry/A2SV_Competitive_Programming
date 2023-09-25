class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        s2=s[-1::-1]
        cache = {}
        def dfs(i,j):
            if(i<0 or j<0):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if(s[i] == s2[j]):
                cache[(i,j)] = 1 + dfs(i-1,j-1)
                return cache[(i,j)]
            cache[(i,j)] = max(dfs(i-1,j),dfs(i,j-1))
            return cache[(i,j)]
        
        return dfs(n-1,n-1)