class Solution:
    def dijkstra(self, signalReceivedAt, source, n):
        pq = []
        heapq.heappush(pq, (0, source))

        signalReceivedAt[source] = 0

        while pq:
            currNodeTime, currNode = heapq.heappop(pq)

            if currNodeTime > signalReceivedAt[currNode]:
                continue

            for time, neighborNode in self.adj[currNode]:
                if signalReceivedAt[neighborNode] > currNodeTime + time:
                    signalReceivedAt[neighborNode] = currNodeTime + time
                    heapq.heappush(pq, (signalReceivedAt[neighborNode], neighborNode))
        

    def networkDelayTime(self, times, n, k):
        self.adj = defaultdict(list)

        for time in times:
            source = time[0]
            dest = time[1]
            travelTime = time[2]

            self.adj[source].append((travelTime, dest))

        signalReceivedAt = [float('inf')] * (n + 1)
        self.dijkstra(signalReceivedAt, k, n)

        answer = float('-inf')
        for i in range(1, n + 1):
            answer = max(answer, signalReceivedAt[i])

        return -1 if answer == float('inf') else answer