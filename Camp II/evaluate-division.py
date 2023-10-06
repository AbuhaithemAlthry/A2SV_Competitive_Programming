class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def dfs(st, en, res, visited):
            if st == en:
                return res
            
            visited.add(st)
            tmp = -1.0
            for i,w in graph[st]:
                if i not in visited:
                    tmp = dfs(i, en, res * w, visited)
                    if tmp != -1.0:
                        break
            
            return tmp

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                visited=set()
                res.append(dfs(a,b,1,visited))
        return res
