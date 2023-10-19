class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-frequency,string) for string ,frequency in counter.items()]
        heapq.heapify(heap)
        ans = ""
        while heap:
            fr,st = heapq.heappop(heap)
            ans+=(-fr*st)
        return ans