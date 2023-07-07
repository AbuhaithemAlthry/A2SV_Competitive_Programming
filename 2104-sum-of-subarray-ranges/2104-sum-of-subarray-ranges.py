class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0 
        stack = []

        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                count = (mid - left) * (right - mid)
                answer -= nums[mid] * count
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                count = (mid - left) * (right - mid)
                answer += nums[mid] * count
            stack.append(right)

        return answer
