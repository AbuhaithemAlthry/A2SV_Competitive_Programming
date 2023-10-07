class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == n1-1 and j == n2-1:
                if nums1[i]==nums2[j]:
                    return 1
                return 0
            if i >= n1 or j >= n2:
                return 0
            if nums1[i]==nums2[j]:
                memo[(i,j)] = 1 + dp(i+1,j+1)
                return memo[(i,j)]
            
            takeFromFirst = dp(i+1,j)
            takeFromSecond = dp(i,j+1)
            memo[(i,j)] = max(takeFromFirst, takeFromSecond)
            return memo[(i,j)]
        
        return dp(0,0)