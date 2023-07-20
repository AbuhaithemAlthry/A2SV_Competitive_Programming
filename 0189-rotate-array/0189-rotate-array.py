class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = 0
        # r = k
        # tempList = nums[:]
        # while l < len(nums):
        #     r = r % len(nums)
        #     nums[r] = tempList[l]
        #     l += 1
        #     r +=1
        
        k = k % len(nums)
        l, r= 0, len(nums) - 1
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r=l+1,r-1
        print(nums)
        l,r=0, k-1
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r=l+1,r-1
        print(nums)
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r=l+1,r-1