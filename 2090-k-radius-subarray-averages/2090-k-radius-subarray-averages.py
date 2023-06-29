class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l,r,n = 0,0,len(nums)
        res = [-1]*n
        sum_=0
        while r < n:
            sum_+=nums[r]
            if r >= 2*k:
                res[(l+r)//2]=sum_//(r-l+1)
                sum_-=nums[l]
                l+=1
            r+=1
        return res
            