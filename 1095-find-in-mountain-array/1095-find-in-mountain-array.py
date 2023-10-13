class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left,right = -1, mountain_arr.length()
        N = mountain_arr.length()
        while right > left + 1:
            md = left + (right - left) // 2
            currValue = mountain_arr.get(md)
            nxtValue = mountain_arr.get(md + 1) if md + 1 < N else float("-inf")
            
            if currValue >= nxtValue:
                right = md
                
            else:
                left = md
         
        peak = right
 
        def binRight(left,right):
            while right > left + 1:
                md = left + (right - left) // 2
                currValue = mountain_arr.get(md)

                if currValue <= target:
                    right = md 

                else:
                    left = md 
        
            return right
        
        def binLeft(left,right):
            while right > left + 1:
                md = left + (right - left) // 2
                currValue = mountain_arr.get(md)

                if currValue >= target:
                    right = md

                else:
                    left = md
                    
            return right

        leftRes = binLeft(-1,peak + 1)
        rightRes = binRight(peak - 1,N)

        ans = -1
        if rightRes < N:
            ans = rightRes if mountain_arr.get(rightRes) == target else ans
        
        if leftRes >= 0:
            ans = leftRes if mountain_arr.get(leftRes) == target else ans
    
        return ans
        