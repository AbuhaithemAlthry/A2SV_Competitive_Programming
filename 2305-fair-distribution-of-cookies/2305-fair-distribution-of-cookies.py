class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        n = len(cookies)
        
        def backtrack(i, zer):
            
            if n-i < zer:
                return float('inf')
            
            if n==i:
                return max(cur)
            
            answer = float('inf')
            
            for j in range(k):
                zer -= int(cur[j]==0)
                cur[j] += cookies[i]
                
                answer = min(answer,backtrack(i+1, zer))
                
                cur[j] -= cookies[i]
                zer += int(cur[j]==0)
                
            return answer
        return backtrack(0,k)