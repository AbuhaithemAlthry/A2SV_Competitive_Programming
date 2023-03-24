class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            if nums[i] < n and pos != i:
                nums[i],nums[pos]=nums[pos],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i:
                return i
        return n

            
