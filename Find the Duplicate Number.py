# since you asked the question in cylclic sorting I did using that but the question said that "You must solve the problem without modifying the array nums and uses only constant extra space."
# the required solution on the leetcode platform is to solve the question by one pass using counting dictionary
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            while (nums[i] != nums[pos-1]) and (i != nums[i]-1):
                nums[i],nums[pos-1]=nums[pos-1],nums[i]
                pos = nums[i]
            i+=1

        for i in range(n):
            if i+1 != nums[i]:
                res=nums[i]
        return res
