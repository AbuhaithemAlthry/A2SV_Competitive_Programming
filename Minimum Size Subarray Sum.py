class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)
        sum_= 0
        min_ =  n + 1
        while r < n :
            sum_ += nums[r]
            while sum_ >= target:
                min_ = min(r-l+1,min_)
                sum_ -= nums[l]
                l += 1
            r += 1
        return min_ if min_!= n+1 else 0
