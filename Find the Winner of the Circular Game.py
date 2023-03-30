class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans, count = [], 1
        
        for i in range(1,n+1):
            ans.append(i)
            
        while len(ans) > 1:
            if count == k:
                a = ans.pop(0)
                count = 1
            else:
                ans.append(ans[0])
                ans.pop(0)
                count += 1
        return ans[0]
