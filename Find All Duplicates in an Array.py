class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            while (nums[i] != nums[pos-1]) and (i != nums[i]-1):
                nums[i],nums[pos-1]=nums[pos-1],nums[i]
                pos = nums[i]
            i+=1
        res=[]
        print(nums)
        for i in range(n):
            if i+1 != nums[i]:
                res.append(nums[i])
        return res
