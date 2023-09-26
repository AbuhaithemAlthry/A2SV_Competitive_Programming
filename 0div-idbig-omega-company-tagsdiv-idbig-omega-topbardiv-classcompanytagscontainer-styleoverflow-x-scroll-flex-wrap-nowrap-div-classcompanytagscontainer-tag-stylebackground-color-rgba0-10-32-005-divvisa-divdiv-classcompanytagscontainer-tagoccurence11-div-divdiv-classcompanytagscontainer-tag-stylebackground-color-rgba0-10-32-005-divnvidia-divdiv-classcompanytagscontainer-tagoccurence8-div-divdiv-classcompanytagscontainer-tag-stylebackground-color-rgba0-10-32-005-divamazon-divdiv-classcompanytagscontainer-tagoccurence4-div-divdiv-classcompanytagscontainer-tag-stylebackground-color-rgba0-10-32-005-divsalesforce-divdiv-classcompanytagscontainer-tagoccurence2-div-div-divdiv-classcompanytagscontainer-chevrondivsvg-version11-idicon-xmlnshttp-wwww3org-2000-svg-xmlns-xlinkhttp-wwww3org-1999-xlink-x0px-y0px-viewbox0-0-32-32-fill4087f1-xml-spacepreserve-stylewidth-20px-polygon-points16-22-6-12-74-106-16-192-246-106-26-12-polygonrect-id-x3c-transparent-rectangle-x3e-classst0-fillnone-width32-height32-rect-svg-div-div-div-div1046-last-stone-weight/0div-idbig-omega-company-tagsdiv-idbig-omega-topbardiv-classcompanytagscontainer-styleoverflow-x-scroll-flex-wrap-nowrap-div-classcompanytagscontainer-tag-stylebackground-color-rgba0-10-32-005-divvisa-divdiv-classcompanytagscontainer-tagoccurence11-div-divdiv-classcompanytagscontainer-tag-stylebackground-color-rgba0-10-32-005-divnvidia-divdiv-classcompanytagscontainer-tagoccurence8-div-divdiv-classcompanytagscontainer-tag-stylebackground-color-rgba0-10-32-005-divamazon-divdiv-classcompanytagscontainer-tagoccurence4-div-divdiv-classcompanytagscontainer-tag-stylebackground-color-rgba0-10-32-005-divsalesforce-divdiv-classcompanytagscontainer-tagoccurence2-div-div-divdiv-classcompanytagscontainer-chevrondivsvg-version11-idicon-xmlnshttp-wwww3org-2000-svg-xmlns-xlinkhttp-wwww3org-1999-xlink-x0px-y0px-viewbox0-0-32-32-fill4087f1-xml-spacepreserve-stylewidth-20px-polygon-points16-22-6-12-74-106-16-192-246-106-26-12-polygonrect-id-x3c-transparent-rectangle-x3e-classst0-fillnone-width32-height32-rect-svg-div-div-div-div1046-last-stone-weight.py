class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heappush(heap,-num) 
        while len(heap)>1:
            x=heappop(heap)
            y=heappop(heap)
            if -x==-y:
                continue
            if -x>-y:
                heappush(heap,-(-x+y))
            elif -x < -y:
                heappush(heap,-(-y+x))
        return -heap[0] if heap else 0