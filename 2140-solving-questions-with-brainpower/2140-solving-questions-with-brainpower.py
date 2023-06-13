class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache={}
        def dp(i):
            if i > len(questions)-1:
                return 0
            if i not in cache:
                max_=max(
                dp(i+1),
                questions[i][0] + dp(i+questions[i][1]+1)
                )
                cache[i] = max_
            return cache[i]
        
        return dp(0)