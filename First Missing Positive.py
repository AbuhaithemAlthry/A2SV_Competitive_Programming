class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            while (0 < pos <= n) and(nums[i] != nums[pos-1]) and (i != nums[i]-1):
                nums[i],nums[pos-1]=nums[pos-1],nums[i]
                pos = nums[i]
            i+=1
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
