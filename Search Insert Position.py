class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = -1,len(nums)
        while r > l+1:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        return r 
