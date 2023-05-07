class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        counts = Counter(words)

        heap = [(-count, word) for word, count in counts.items()]

        res = heapq.nsmallest(k, heap)

        return [word for _, word in res]