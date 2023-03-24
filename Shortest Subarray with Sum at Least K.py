class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = collections.deque([[0, 0]])
        res, cur_sum = float('inf'), 0
        for i, a in enumerate(nums):
            cur_sum += a
            while dq and cur_sum - dq[0][1] >= k:
                res = min(res, i + 1 - dq.popleft()[0])
            while dq and cur_sum <= dq[-1][1]:
                dq.pop()
            dq.append([i + 1, cur_sum])
        return res if res != float('inf') else -1
