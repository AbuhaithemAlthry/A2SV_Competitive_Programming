class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)
        while r >= l:
            mid = l+(r-l)//2
            mid_val = nums[mid]
            left = nums[mid-1] if mid > 0 else float('-inf')
            right = nums[mid+1] if mid < len(nums)-1 else float('-inf')
            if left < mid_val > right:
                return mid
            elif left < mid_val < right:
                l = mid+1
            else:
                r = mid-1
        return 0
