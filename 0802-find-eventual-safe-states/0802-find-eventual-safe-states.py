class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node: int) -> int:
            if visited[node] != 0:
                return visited[node]
            visited[node] = 1
            for neighbor in graph[node]:
                if dfs(neighbor) == 1:
                    return 1
            visited[node] = 2
            return 2
        
        n = len(graph)
        visited = [0] * n
        return [i for i in range(n) if dfs(i) == 2]