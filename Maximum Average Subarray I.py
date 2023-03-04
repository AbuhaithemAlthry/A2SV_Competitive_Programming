class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r =0,0
        n = len(nums)
        sum_ = 0
        res = []
        while r<n:
            sum_ += nums[r]
            if r >= k-1:
                res.append(sum_/k)
                sum_ -= nums[l]
                l +=1
            r += 1
        return max(res)
