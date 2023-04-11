class Solution:
    def build(self,edges):
        graph = defaultdict(list) 
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
        return graph
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.build(edges)
        def dfs(source, visited):
            visited.add(source)
            if source == destination:
                return True
            for neighbour in graph[source]:
                if neighbour not in visited:
                    found = dfs(neighbour,arr)
                    if found:
                        return True
        arr = set()
        return dfs(source,arr)