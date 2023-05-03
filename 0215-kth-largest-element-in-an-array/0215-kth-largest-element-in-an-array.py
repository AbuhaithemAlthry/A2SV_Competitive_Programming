class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-nums[i] for i in range(len(nums))]
        heapq.heapify(res)
        for j in range(k):
            a = heapq.heappop(res)
        return -1*a