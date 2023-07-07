class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        MOD = (10**9) + 7
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_bound = -1 if not stack else stack[-1]
                right_bound = i
                count = (mid - left_bound) * (right_bound - mid)
                res += (count * arr[mid])
            stack.append(i)
        return res % MOD
                