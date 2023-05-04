class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        while len(heap) > 1:
            x = heappop(heap)
            if heap[0] == x:
                heappop(heap)
            else:
                heappush(heap, x - heappop(heap))
        return -heap[0] if heap else 0