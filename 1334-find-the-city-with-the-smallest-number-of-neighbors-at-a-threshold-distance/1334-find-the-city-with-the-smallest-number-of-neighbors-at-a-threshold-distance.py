class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
        ans = 0
        min_neighbors = float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold and dist[i][j] != 0:
                    count += 1
            if count <= min_neighbors:
                min_neighbors = count
                ans = i
        return ans