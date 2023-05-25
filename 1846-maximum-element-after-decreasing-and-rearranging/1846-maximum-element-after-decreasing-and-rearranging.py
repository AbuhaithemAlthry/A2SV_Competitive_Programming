class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        if len(arr)==1:
            return 1
        
        arr.sort()
        flag = 0
        for i in range(1,len(arr)):
            if arr[0]!=1:
                flag = 1
                break
            if (arr[i] - arr[i-1]) > 1:
                flag = 1
                break
        if flag:
            if arr[0]!=1:
                arr[0] = 1
            for i in range(1,len(arr)):
                if (arr[i] - arr[i-1]) > 1:
                    arr[i]=arr[i-1]+1
            
        return max(arr)