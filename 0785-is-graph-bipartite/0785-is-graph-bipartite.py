class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graphBuild = defaultdict(list)
        for i in range(len(graph)):
            for child in graph[i]:
                graphBuild[i].append(child)
                
                
        n = len(graph)
        colors = [0]*n
        
        def dfs(node,color):
            for nei in graph[node]:
                if colors[nei] == 0:
                    colors[nei] = color
                    if not dfs(nei,-1 * color):
                        return False
                else:
                    if colors[nei] == colors[node]:
                        return False
            return True
        for i in range(len(graph)):
            if colors[i] == 0:
                if not dfs(i,1):
                    return False
        return True
            
                    
                    