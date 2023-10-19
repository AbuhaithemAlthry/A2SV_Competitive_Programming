class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-j,i) for i,j in counter.items()]
        heapq.heapify(heap)
        ans = []
        
        while k > 0:
            fr,num = heapq.heappop(heap)
            ans.append(num)
            k-=1
        return ans