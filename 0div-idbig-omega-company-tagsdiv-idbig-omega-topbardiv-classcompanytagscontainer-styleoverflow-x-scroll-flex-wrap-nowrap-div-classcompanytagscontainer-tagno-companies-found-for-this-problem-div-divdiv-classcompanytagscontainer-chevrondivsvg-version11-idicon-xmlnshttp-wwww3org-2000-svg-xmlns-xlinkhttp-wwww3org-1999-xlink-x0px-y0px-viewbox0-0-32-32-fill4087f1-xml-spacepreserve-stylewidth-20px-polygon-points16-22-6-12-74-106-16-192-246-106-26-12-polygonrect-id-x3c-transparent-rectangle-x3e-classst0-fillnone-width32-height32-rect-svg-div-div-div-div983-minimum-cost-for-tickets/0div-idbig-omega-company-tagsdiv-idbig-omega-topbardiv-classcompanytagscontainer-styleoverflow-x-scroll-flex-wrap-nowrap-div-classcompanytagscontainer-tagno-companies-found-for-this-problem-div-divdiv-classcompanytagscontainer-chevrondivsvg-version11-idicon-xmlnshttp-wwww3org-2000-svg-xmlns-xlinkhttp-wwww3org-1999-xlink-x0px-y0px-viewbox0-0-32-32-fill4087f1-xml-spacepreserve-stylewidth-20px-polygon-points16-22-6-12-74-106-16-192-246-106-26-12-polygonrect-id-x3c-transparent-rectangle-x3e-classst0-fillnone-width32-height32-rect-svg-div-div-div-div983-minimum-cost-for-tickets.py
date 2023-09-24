class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        
        def dfs(i):
            if i==len(days):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i]= float('inf')
            for d,c in zip([1,7,30],costs):
                j = i
                while j<len(days) and days[j] < days[i]+d:
                    j+=1
                memo[i] = min(memo[i], dfs(j)+c)
            return memo[i]
        
        return dfs(0)
                