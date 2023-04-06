class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_ = max(arr)
        max_ind = arr.index(max_)

        if len(arr)<3:
            return False
 
        if max_ind == len(arr)-1 or max_ind == 0:
            return False
            
        for i in range(1,len(arr)):
            if arr[i] == max_:
                imax = i
                break
            if arr[i] <= arr[i-1]:
                return False
        for i in range(imax+1,len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        return True
