class Solution:
    def build(self,edges):
        graph = defaultdict(list) 
        for i,d in enumerate(edges):
            for num in d:
                graph[i].append(num)
        return graph
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_d = self.build(graph)
        ans = []
        def dfs(src,path):
            if src == len(graph)-1:
                ans.append(path[:])
                return
            for neighbour in graph_d[src]:
                path.append(neighbour)
                dfs(neighbour,path)
                path.pop()
        dfs(0,[0])
        return ans