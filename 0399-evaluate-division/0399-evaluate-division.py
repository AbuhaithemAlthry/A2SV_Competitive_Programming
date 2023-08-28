class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
        
        def dfs(st,en,res):
            # if st in visited:
            #     return -1.0
            
            if st == en:
                return res
            
            visited.add(st)
            
            for i in graph[st]:
                if i not in visited:
                    tmp = dfs(i,en,res*graph[st][i])
                    if tmp != -1.0:
                        return tmp

            return -1.0
        dfs
        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                visited=set()
                res.append(dfs(a,b,1))
        return res