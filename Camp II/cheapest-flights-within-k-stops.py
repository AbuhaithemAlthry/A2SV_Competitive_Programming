class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
        seen = {}
        heap = []
        heappush(heap, (0, 0, src))
        
        while heap:
            cost, hops, city = heappop(heap)
            seen[city] = hops
            
            if city == dst:
                return cost
            
            if hops > k:
                continue

            for next_city, next_cost in graph[city]:
                
                if next_city in seen and seen[next_city] <= hops:
                    continue
                heappush(heap, (cost + next_cost, hops + 1, next_city))
        
        return -1
