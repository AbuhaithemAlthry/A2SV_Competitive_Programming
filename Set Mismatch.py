class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            pos = nums[i]
            while nums[i]!=nums[pos-1] and i != pos-1:
                nums[i],nums[pos-1]=nums[pos-1],nums[i]
                pos=nums[i]
            i+=1
        res = []
        for i in range(n):
            if i != nums[i]-1:
                res.append(nums[i])
                res.append(i+1)
        return res
