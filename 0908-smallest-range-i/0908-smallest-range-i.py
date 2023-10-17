class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        if max_-min_ <= 2*k:
            return 0
        else:
            return (max_ - min_) - 2*k