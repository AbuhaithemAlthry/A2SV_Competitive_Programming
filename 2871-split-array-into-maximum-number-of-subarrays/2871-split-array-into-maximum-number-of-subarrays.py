class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minScore = nums[0]
        for i in range(1,len(nums)):
            minScore &= nums[i]

        if minScore > 0:
            return 1


        subarrayCount = 0
        currScore = (1 << 32) - 1
        for num in nums:
            currScore &= num
            if currScore == 0:
                subarrayCount += 1
                currScore = (1 << 32) - 1
        
        return subarrayCount