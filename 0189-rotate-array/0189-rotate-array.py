class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = k
        tempList = nums[:]
        while l < len(nums):
            r = r % len(nums)
            nums[r] = tempList[l]
            l += 1
            r +=1