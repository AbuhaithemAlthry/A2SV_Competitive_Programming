class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            while (nums[i] != nums[pos-1]) and (i != nums[i]-1):
                nums[i],nums[pos-1]=nums[pos-1],nums[i]
                pos = nums[i]
            i+=1
        res=[]
        for i in range(n):
            if i+1 != nums[i]:
                res.append(i+1)
        return res
