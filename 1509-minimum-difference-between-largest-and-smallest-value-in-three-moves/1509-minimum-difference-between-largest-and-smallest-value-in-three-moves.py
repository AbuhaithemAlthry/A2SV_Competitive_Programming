class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        n = len(nums)-1
        nums.sort()
        min_=[]
        min_.append(nums[n]-nums[3])
        min_.append(nums[n-3]-nums[0])
        min_.append(nums[n-1]-nums[2])
        min_.append(nums[n-2]-nums[1])
        return min(min_)
            
        