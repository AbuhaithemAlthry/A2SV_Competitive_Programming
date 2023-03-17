class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #edge case if nums is empty
        if nums == []:
            return [-1,-1]
        
        #the first binary search
        l=-1
        r=len(nums)
        while r > l+1:
            mid = (l+r)//2
            if nums[mid] >= target:
                r=mid
            else:
                l=mid
        if not 0 <=r<=len(nums)-1 or nums[r] != target:
            return [-1,-1]
        
        #saving the first value of binary search in a
        a = r
        
        #the second binary search
        l = r-1
        r = len(nums)
        while r > l+1:
            mid = (l+r)//2
            if nums[mid] > target:
                r=mid
            else:
                l=mid
        #saving the second value of binary search in b
        b = r-1

        return [a,b]
