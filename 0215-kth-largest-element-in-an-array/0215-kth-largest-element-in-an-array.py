class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-nums[i] for i in range(len(nums))]
        heapq.heapify(res)
        for j in range(k-1):
            heapq.heappop(res)
        return -heapq.heappop(res)